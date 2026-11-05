# app/rag_pipeline.py

import os
import re
import unicodedata
from langchain.globals import set_verbose, get_verbose

set_verbose(True)  # Si quieres ver logs detallados

from app.llm_provider import get_llm, get_embeddings, get_vectorstore_dir, describe
from app.prompt_registry import DEFAULT_PROMPT, load_prompt_text, list_prompt_options

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_core.retrievers import BaseRetriever
from langchain.chains import ConversationalRetrievalChain
from rank_bm25 import BM25Okapi

from dotenv import load_dotenv
import mlflow

load_dotenv()

DATA_DIR = "data/pdfs"
VECTOR_DIR = get_vectorstore_dir()  # vectorstore/openai o vectorstore/fastembed

# Nombre legible de cada PDF: el modelo lo recibe junto al fragmento para poder citarlo
DOCUMENT_NAMES = {
    "piscc-medellin-2024-2027.pdf": "PISCC 2024-2027",
    "Diagnostico_Politica_Publica.pdf": "Diagnóstico para la política pública de seguridad y convivencia",
    "Plan_Desarrollo_Seguridad_2024-2027.pdf": "Plan de Desarrollo Distrital 2024-2027",
}
DOCUMENT_PROMPT = PromptTemplate.from_template("[Documento: {documento}]\n{page_content}")

def load_documents(path=DATA_DIR):
    docs = []
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(path, file))
            pages = loader.load()
            for page in pages:
                page.metadata["documento"] = DOCUMENT_NAMES.get(file, os.path.splitext(file)[0])
            docs.extend(pages)
    return docs

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE") or 512)
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP") or 50)

def save_vectorstore(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP, persist_path=VECTOR_DIR):
    docs = load_documents()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_documents(docs)
    embeddings = get_embeddings()
    vectordb = FAISS.from_documents(chunks, embedding=embeddings)
    vectordb.save_local(persist_path)

    mlflow.set_experiment("vectorstore_tracking")
    with mlflow.start_run(run_name="vectorstore_build"):
        mlflow.log_param("chunk_size", chunk_size)
        mlflow.log_param("chunk_overlap", chunk_overlap)
        mlflow.log_param("n_chunks", len(chunks))
        mlflow.log_param("n_docs", len(docs))
        mlflow.log_params(describe())
        mlflow.set_tag("vectorstore", persist_path)

def load_vectorstore(chunk_size=512, chunk_overlap=50):
    docs = load_documents()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_documents(docs)
    embeddings = get_embeddings()
    return FAISS.from_documents(chunks, embedding=embeddings)

def load_vectorstore_from_disk(persist_path=VECTOR_DIR):
    if not os.path.exists(persist_path):
        raise FileNotFoundError(
            f"No existe el índice en '{persist_path}'. Genéralo primero con: "
            'python -c "from app.rag_pipeline import save_vectorstore; save_vectorstore()"'
        )
    embeddings = get_embeddings()
    return FAISS.load_local(persist_path, embeddings, allow_dangerous_deserialization=True)

def load_prompt(version=DEFAULT_PROMPT):
    """
    Carga el prompt desde el Prompt Registry de MLflow (prompts:/nombre@alias)
    o desde un archivo local de app/prompts/ (nombre sin .txt).
    La URI resuelta queda en prompt.metadata["prompt_uri"].
    """
    prompt_text, uri = load_prompt_text(version)
    return PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_text,
        metadata={"prompt_uri": uri},
    )

def list_prompt_versions():
    """Alias y versiones disponibles en el registro (o archivos locales si no hay registro)."""
    return list_prompt_options()

# Modo de recuperación:
#   vector   similitud de embeddings, entrega fragmentos
#   palabras BM25 con el nombre del documento, entrega páginas completas
#   union    vector + palabras, entrega páginas completas
RETRIEVER_MODES = ("vector", "palabras", "union")
_STOPWORDS = set("""a al algo como con cual cuales cuantas cuantos de del desde el ella en entre es esa
    ese esta este fue fueron la las lo los mas no o para por que se segun si sobre son su sus un una y""".split())

def get_retriever_mode():
    mode = (os.getenv("RETRIEVER_MODE") or "vector").strip().lower()
    if mode not in RETRIEVER_MODES:
        raise ValueError(f"RETRIEVER_MODE no soportado: '{mode}'. Usa uno de: {RETRIEVER_MODES}")
    return mode

def _tokens(text):
    """Minúsculas, sin acentos ni palabras vacías; conserva cifras como 12,82 o 475.203."""
    plain = "".join(c for c in unicodedata.normalize("NFD", text.lower()) if unicodedata.category(c) != "Mn")
    return [w for w in re.findall(r"[a-z0-9.,%]*[a-z0-9%]", plain) if w not in _STOPWORDS]

class PageRetriever(BaseRetriever):
    """Busca fragmentos y devuelve la página completa de cada uno, sin repetirlas."""
    vectordb: object
    fragments: list
    bm25: object
    pages: dict
    k: int = 4
    mode: str = "palabras"

    def _get_relevant_documents(self, query, *, run_manager=None):
        hits = []
        if self.mode == "union":
            hits += self.vectordb.similarity_search(query, k=self.k)
        scores = self.bm25.get_scores(_tokens(query))
        top = sorted(range(len(self.fragments)), key=lambda i: -scores[i])[:self.k]
        hits += [self.fragments[i] for i in top]

        keys = dict.fromkeys((d.metadata["documento"], d.metadata["page"]) for d in hits)
        return [self.pages[key] for key in keys]

def build_retriever(vectordb, k=4):
    mode = get_retriever_mode()
    if mode == "vector":
        return vectordb.as_retriever(search_kwargs={"k": k})

    fragments = list(vectordb.docstore._dict.values())
    grouped = {}
    for fragment in fragments:
        key = (fragment.metadata["documento"], fragment.metadata["page"])
        grouped.setdefault(key, []).append(fragment)
    pages = {
        key: Document(page_content="\n".join(f.page_content for f in group), metadata=group[0].metadata)
        for key, group in grouped.items()
    }
    bm25 = BM25Okapi([_tokens(f"{f.metadata['documento']} {f.page_content}") for f in fragments])
    return PageRetriever(vectordb=vectordb, fragments=fragments, bm25=bm25, pages=pages, k=k, mode=mode)

def build_chain(vectordb, prompt_version=DEFAULT_PROMPT, k=4):
    prompt = load_prompt(prompt_version)
    retriever = build_retriever(vectordb, k=k)
    return ConversationalRetrievalChain.from_llm(
        llm=get_llm(temperature=0),
        retriever=retriever,
        combine_docs_chain_kwargs={"prompt": prompt, "document_prompt": DOCUMENT_PROMPT},
        return_source_documents=True  # para mostrar las referencias en la UI
    )
