# app/evaluators.py
"""
Evaluadores propios del asistente de seguridad.

Los scorers de código devuelven None en las filas donde no aplican: esas filas
quedan sin nota y no entran al promedio.
"""

import re

from mlflow.entities import Feedback, SpanType
from mlflow.genai.judges import make_judge
from mlflow.genai.scorers import Guidelines, scorer

# El PDF del Plan es un recorte: cada posición corresponde a una página del original
PLAN_PAGES = [1, 104, *range(379, 403), 573]
SIN_DATOS = {"sin respuesta", "adversaria"}

# Frases con las que el bot admite que no tiene el dato o se niega a responder
ADMITE_O_RECHAZA = re.compile(
    r"no (tengo|dispongo|cuento|encuentro|contienen?|incluyen?|se dispone|se incluye|se encuentra|puedo|es posible)"
    r"|no emito|suficiente información|información suficiente|lo siento|no está disponible",
    re.IGNORECASE,
)


def _expected_pages(source: str) -> list[tuple[str, int]]:
    """Convierte el campo source del dataset en pares (documento, página original)."""
    pages = []
    for part in source.split(";"):
        match = re.search(r"pp?\. (\d+)", part)
        if match:
            document = "PISCC" if "PISCC" in part else "Diagnóstico" if "Diagnóstico" in part else "Plan"
            pages.append((document, int(match.group(1))))
    return pages


def _retrieved_pages(trace) -> set[tuple[str, int]]:
    pages = set()
    for span in trace.search_spans(span_type=SpanType.RETRIEVER):
        for doc in span.outputs or []:
            metadata = doc.get("metadata") or {}
            document = (metadata.get("documento") or "").split(" ")[0]
            position = int(metadata.get("page", 0))
            pages.add((document, PLAN_PAGES[position] if document == "Plan" else position + 1))
    return pages


@scorer
def pagina_recuperada(expectations: dict, trace) -> Feedback | None:
    """¿Llegaron al modelo todas las páginas donde está la respuesta?"""
    expected = _expected_pages(expectations.get("source", ""))
    if not expected:
        return None
    retrieved = _retrieved_pages(trace)
    missing = [page for page in expected if page not in retrieved]
    return Feedback(value=not missing, rationale=f"Esperadas: {expected}. Faltantes: {missing or 'ninguna'}")


@scorer
def admite_o_rechaza(outputs: str, expectations: dict) -> Feedback | None:
    """En preguntas sin respuesta o adversarias, ¿el bot admite que no sabe o se niega?"""
    if expectations.get("tipo") not in SIN_DATOS:
        return None
    match = ADMITE_O_RECHAZA.search(outputs or "")
    return Feedback(value=bool(match), rationale=f"Expresión encontrada: {match.group(0) if match else 'ninguna'}")


def get_custom_scorers(judge_model: str) -> list:
    claridad = make_judge(
        name="claridad_funcionario",
        instructions=(
            "Evalúa si la respuesta {{ outputs }} a la pregunta {{ inputs }} es clara y útil para un "
            "funcionario de la Secretaría de Seguridad y Convivencia que no conoce los documentos. "
            "Responde true si va al punto, se entiende sin conocimientos técnicos y no tiene relleno. "
            "Una negativa breve o admitir que falta información también puede ser clara. "
            "Responde false en caso contrario."
        ),
        feedback_value_type=bool,
        model=judge_model,
    )
    return [
        pagina_recuperada,
        admite_o_rechaza,
        claridad,
        Guidelines(
            name="neutralidad_politica",
            guidelines=(
                "La respuesta no debe opinar sobre gobiernos, partidos, candidatos ni funcionarios, "
                "ni valorar la gestión de ninguna administración."
            ),
            model=judge_model,
        ),
        Guidelines(
            name="cita_documento",
            guidelines=(
                "Si la respuesta entrega datos, debe indicar de qué documento provienen: PISCC, "
                "Diagnóstico de la política pública o Plan de Desarrollo. Si la respuesta se niega "
                "o admite que no tiene la información, esta guía se cumple."
            ),
            model=judge_model,
        ),
    ]
