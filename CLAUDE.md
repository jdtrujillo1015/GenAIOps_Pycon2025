# CLAUDE.md — Taller GenAIOps (Experiencias en Analítica)

## Contexto
- Segundo trabajo del curso *Experiencias en Analítica*. Es en equipo.
- Repo: fork `jdtrujillo1015/GenAIOps_Pycon2025` (upstream: `darkanita/GenAIOps_Pycon2025`).
- La base es un chatbot RAG de Recursos Humanos (Contoso). Hay que adaptarlo a un dominio propio.
- La guía oficial es **`DESAFIO.md`**: léela completa antes de cambiar nada; manda sobre este archivo.
- Entrega estimada: **viernes 13 de noviembre de 2026**. Se sustenta en 15–20 min por Teams.

## Dominio elegido
Asistente para la **Secretaría de Seguridad y Convivencia** de Medellín. Corpus de 421 páginas:
1. **PISCC 2024-2027**, completo (288 págs.): `piscc-medellin-2024-2027.pdf`
2. **Diagnóstico para la política pública** de seguridad y convivencia (106 págs.): `Diagnostico_Politica_Publica.pdf`. Es solo diagnóstico: no trae objetivos ni líneas de la política.
3. **Plan de Desarrollo 2024-2027, parte de seguridad** (27 págs.): `Plan_Desarrollo_Seguridad_2024-2027.pdf`

Los PDFs van en `data/pdfs/` y reemplazan los de RRHH.

El recorte del Plan toma estas páginas del original: 1, 104, 379-402 y 573. El PDF completo queda en `data/fuentes/`, fuera de git. En el campo `source` del dataset se citan las páginas del original (salen impresas en cada página), no la posición en el recorte.

## Stack del repo
- RAG con LangChain, vector store FAISS y UI en Streamlit.
- `app/llm_provider.py` selecciona el proveedor (OpenAI o Groq) desde `.env` con `LLM_PROVIDER` y `GROQ_API_KEY`. Con Groq, los embeddings se calculan en local con FastEmbed.
- `app/prompt_registry.py` usa el MLflow Prompt Registry, con versiones y alias como `@production`.
- `app/prompts/` contiene las plantillas del RAG. Cada una **debe** incluir `{context}` y `{question}`.
- `app/run_eval.py` corre `mlflow.genai.evaluate` con estos scorers: Correctness, RelevanceToQuery, RetrievalGroundedness, RetrievalRelevance, Safety y Guidelines (`idioma_espanol`, `tono_profesional`).
- `app/tracking.py` define `CHAT_EXPERIMENT`.
- `tests/eval_dataset.json` es el dataset de evaluación.
- `.github/workflows/eval.yml` es el CI con el quality gate.

## Qué hay que hacer (resumen de DESAFIO.md)
1. **Dominio (10 pts)**
   - Reemplazar los PDFs y las plantillas de `app/prompts/`.
   - Poner `PROMPT_NAME=asistente_seguridad_medellin` en `.env` y cambiar `CHAT_EXPERIMENT`.
   - Cambiar la guideline `tono_profesional`, que hoy menciona RRHH, en `get_scorers()` de `run_eval.py`.
   - Reconstruir el índice y registrar los prompts con `python -m app.prompt_registry`.
2. **Dataset (15 pts)**: al menos 15 preguntas en `tests/eval_dataset.json`.
   - Directas: mínimo 6.
   - Multi-documento: mínimo 3.
   - Sin respuesta: mínimo 3.
   - Adversarias: mínimo 3.
   - Cada respuesta esperada debe verificarse en los PDFs.
3. **Experimentos (20 pts)**
   - Comparar al menos 2 versiones de prompt (`PROMPT_VERSION=prompts:/<nombre>/N python app/run_eval.py`), valores de `k` y tamaños de chunk.
   - Cambiar **una variable a la vez**.
   - Clasificar 5 fallos (recuperación, generación, dataset o juez) con evidencia de las trazas.
   - Al terminar, restaurar la configuración base del índice.
4. **Evaluadores propios (20 pts)**
   - Un scorer de código con `@scorer`.
   - Un juez con `make_judge`, que solo puede usar `{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}` y `{{ trace }}`.
   - Al menos una `Guidelines` propia del dominio.
5. **Confianza en el juez (15 pts)**
   - Calificar 10 respuestas a mano y registrar esas calificaciones en MLflow.
   - Calcular el acuerdo con el juez y repetir con otro modelo juez.
6. **Producción (10 pts)**
   - Promover el mejor prompt con `python -m app.prompt_registry --promote N`.
   - Definir la variable `PROMPT_VERSION` del repo y justificar los umbrales del gate.
   - Dejar el CI en verde.
   - Abrir un PR con un prompt deliberadamente malo y mostrar que el gate lo bloquea.
7. **Informe (10 pts)**: `INFORME.md`, máximo 4 páginas, con capturas de MLflow y del dashboard. Debe responder las 6 preguntas de DESAFIO.md.
8. **Bonus (+10)**: ver DESAFIO.md (comparar versiones en el dashboard, costos, `optimize_prompts`, red teaming, pestaña Judges/Review).

**Entregables:** el fork, `mlflow.db` (o el artefacto `mlflow-db` del último run de Actions) e `INFORME.md`.

## Particularidades del dominio
- **Preguntas multi-documento**: el PISCC, la política y el Plan de Desarrollo se cruzan en metas, programas e indicadores.
- **Preguntas sin respuesta**: cifras recientes de criminalidad, datos que no están en los PDFs o fechas posteriores a los documentos.
- **Preguntas adversarias**: pedir opiniones políticas, juicios sobre la administración o datos personales, e intentos de prompt injection.
- **Guideline de dominio sugerida**: neutralidad política (no opinar sobre gobiernos ni candidatos) y citar el documento y la línea estratégica de origen.
- **Riesgos conocidos**:
  - Las tablas de metas e indicadores se extraen mal del PDF.
  - Los tres documentos usan términos parecidos, así que el retriever puede traer el documento equivocado.
  - Reindexar 300 páginas es lento, así que conviene probar pocos tamaños de chunk.
  - Estos riesgos son buenos insumos para el diagnóstico de fallos.

## Restricciones operativas
- **Límite diario del plan gratuito de Groq.** Cada evaluación completa hace unas 50 llamadas al juez.
  - Mientras se itera, usar pocos jueces o un subconjunto del dataset.
  - Dejar las evaluaciones completas solo para las configuraciones finalistas.
  - Si se agota la cuota, cambiar de modelo juez.
- No subir `.env` ni API keys al repo.
- No romper el contrato de las plantillas (`{context}` y `{question}`).

## Forma de trabajar
- Todo en español: código comentado, prompts, dataset e informe.
- Antes de cambios grandes, proponer un plan corto. Hacer commits pequeños con mensajes claros.
- Guardar la evidencia de cada experimento (run IDs de MLflow, configuración usada) para el informe.
- Respuestas cortas y directas, sin relleno.
