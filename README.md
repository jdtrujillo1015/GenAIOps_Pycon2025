# Asistente de seguridad para Medellín

Chatbot RAG para funcionarios de la **Secretaría de Seguridad y Convivencia de Medellín**, construido y evaluado con prácticas de GenAIOps. Responde con base en documentos de planeación de seguridad, cita de dónde sale cada dato y no opina sobre gobiernos ni candidatos.

Es un trabajo del curso *Experiencias en Analítica*. Los resultados completos están en el [informe](INFORME.md) y la evidencia de cada experimento en la [bitácora](EXPERIMENTOS.md).

## Documentos

El asistente usa 421 páginas, en `data/pdfs/`:

| Documento | Páginas |
|---|---|
| Plan Integral de Seguridad y Convivencia Ciudadana (PISCC) 2024-2027 | 288 |
| Diagnóstico para la política pública de seguridad y convivencia | 106 |
| Plan de Desarrollo 2024-2027, parte de seguridad | 27 |

## Resultados clave

**Configuración en producción:** recuperación `union` (vectores + BM25, entrega páginas completas), `k=6`, chunk 512/50, prompt v3, modelo `gpt-oss-120b` en Groq y juez `gpt-oss-20b`.

| Medición | Base (`vector`, k=4) | Producción (`union`, k=6) |
|---|---|---|
| `correctness` sin adversarias, 18 preguntas | 0.36-0.43 | 0.64-0.85 |
| Calificación humana, 5 preguntas nuevas | 0.40 | 0.80 |
| Tokens por pregunta | 948 | 7.190 |
| Latencia media | 1.46 s | 1.78 s |
| Costo por 1.000 preguntas (estimación de MLflow) | $0.27 | $1.22 |

La columna base usa el prompt v1, salvo la calificación humana, que compara ambas configuraciones con v3.

- **Lo que más mejoró:** cambiar la forma de recuperar. Ajustar `k`, el tamaño de chunk o el prompt no superó a la base.
- **Punto débil:** las preguntas multi-documento (3/12), porque no llegan todas las páginas necesarias.
- **Preguntas sin respuesta:** admitió no tener el dato en todas las corridas finales. El riesgo aparece con contexto parcial.
- **Preguntas adversarias:** `neutralidad_politica`, `safety` y `admite_o_rechaza` dieron 1.00 en las corridas finales.
- **Juez:** coincidió 60% con el criterio humano en las preguntas nuevas (kappa 0.29). Sirve para detectar retrocesos, no como medida absoluta.
- **Quality gate:** bloqueó un prompt deliberadamente malo en el [PR de prueba](https://github.com/jdtrujillo1015/GenAIOps_Pycon2025/pull/2).

El holdout tiene solo 5 preguntas, así que esa diferencia es una señal, no una prueba. `main` pasó el gate con 0.64, a una pregunta del bloqueo.

## Cómo ejecutarlo

Requiere Python 3.10 o superior y una API key de [Groq](https://console.groq.com/) (u OpenAI). Con Groq, los embeddings se calculan en local con FastEmbed.

**1. Instalar**

```bash
git clone https://github.com/jdtrujillo1015/GenAIOps_Pycon2025.git
```

```bash
cd GenAIOps_Pycon2025
```

```bash
python -m venv .venv
```

Activa el entorno con `.venv\Scripts\activate` en Windows o `source .venv/bin/activate` en Linux y macOS.

```bash
pip install -r requirements.txt
```

**2. Configurar**

Copia `.env.example` como `.env` y define al menos:

```text
LLM_PROVIDER=groq
GROQ_API_KEY=tu_llave
RETRIEVER_K=6
CHUNK_SIZE=512
CHUNK_OVERLAP=50
```

No subas `.env` al repositorio.

**3. Preparar prompts e índice**

```bash
python -m app.prompt_registry
```

```bash
python -m app.prompt_registry --promote 3
```

```bash
python -c "from app.rag_pipeline import save_vectorstore; save_vectorstore()"
```

**4. Usar la aplicación**

```bash
streamlit run app/main_interface.py
```

Para ver solo las métricas:

```bash
streamlit run app/dashboard.py
```

**5. Evaluar**

```bash
python app/run_eval.py
```

```bash
pytest tests/test_gate.py tests/test_run_eval.py -v
```

Cada evaluación completa hace unas 200 llamadas al juez. Para gastar menos, limita los jueces con `EVAL_SCORERS=correctness,safety`, pero el gate necesita todas sus métricas.

**6. Inspeccionar trazas y prompts**

```bash
mlflow ui --port 5000 --backend-store-uri sqlite:///mlflow.db
```

Abre `http://localhost:5000`.

## Quality gate

El CI (`.github/workflows/eval.yml`) registra los prompts, reconstruye el índice, evalúa y aplica los umbrales de `app/gate.py`:

| Condición | Mínimo |
|---|---|
| `correctness` sin adversarias | 0.60, con al menos 12 notas válidas |
| `admite_o_rechaza` | 0.85 |
| `neutralidad_politica` | 1.00, con al menos 16 notas válidas |
| `safety` | 0.94, con al menos 16 notas válidas |

Para correrlo en tu fork, crea en GitHub (**Settings → Secrets and variables → Actions**):

| Tipo | Nombre | Valor |
|---|---|---|
| Secret | `GROQ_API_KEY` | Tu llave |
| Variable | `LLM_PROVIDER` | `groq` |
| Variable | `EVAL_MODEL` | `groq:/openai/gpt-oss-20b` |
| Variable | `PROMPT_VERSION` | `prompts:/asistente_seguridad_medellin@v3_precision_neutralidad` |

`PROMPT_VERSION` es necesaria porque `mlflow.db` empieza vacío en cada ejecución del CI y `@production` apuntaría a v1.

## Estructura

| Ruta | Contenido |
|---|---|
| `app/rag_pipeline.py` | Carga de PDFs, índice y modos de recuperación |
| `app/prompts/` | Plantillas del prompt; deben incluir `{context}` y `{question}` |
| `app/prompt_registry.py` | Versiones y alias en MLflow |
| `app/evaluators.py` | Evaluadores propios del dominio |
| `app/run_eval.py` | Evaluación con jueces de MLflow |
| `app/gate.py` | Umbrales del quality gate |
| `app/main_interface.py` | Chat y métricas en Streamlit |
| `tests/eval_dataset.json` | Dataset de 18 preguntas |
| `tests/holdout_dataset.json` | 5 preguntas de validación |
| `evidencia/` | Calificaciones humanas y capturas |

## Documentación

- [INFORME.md](INFORME.md): conclusiones y evidencia.
- [EXPERIMENTOS.md](EXPERIMENTOS.md): bitácora con run IDs, trazas y decisiones.
- [DESAFIO.md](DESAFIO.md): enunciado del taller.

## Créditos

Este proyecto es un fork de [GenAIOps_Pycon2025](https://github.com/darkanita/GenAIOps_Pycon2025), de Ana María López Moreno, que aporta la base del chatbot, la integración con MLflow, el CI y el enunciado del taller. La adaptación al dominio de seguridad y la evaluación son de este equipo.

Se distribuye bajo la [licencia MIT](LICENSE) del proyecto original. Los documentos de `data/pdfs/` pertenecen a sus autores institucionales.
