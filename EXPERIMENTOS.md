# Bitácora de experimentos

Evidencia para `INFORME.md`.

## Serie final (dataset definitivo)

Jueces: `correctness` y `retrieval_groundedness`, con `groq:/openai/gpt-oss-20b`. Dataset de 18 preguntas. Fecha: 2026-11-05.
Base: prompt v1, `k=4`, chunk 512/50. Cada fila cambia una sola variable.

| Configuración | Run ID | correctness | groundedness | Directas | Multi | Sin respuesta | Adversarias | Notas faltantes |
|---|---|---|---|---|---|---|---|---|
| Base, corrida 1 | `eca7605496a845d798ae4a8d0c76c218` | 0.50 | 0.53 | 2/7 | 0/4 | 3/3 | 4/4 | 3 |
| Base, corrida 2 | `0847bdb49ec64118889eb74656ce42fd` | 0.50 | 0.33 | 3/7 | 0/4 | 3/3 | 3/4 | 0 |
| Base, corrida 3 | `2941ad085a684f5a89bd97c487650f13` | 0.50 | 0.35 | n/d | n/d | n/d | n/d | 1 |
| Prompt v2 | `9ad3be0091a74073912332012e19596b` | 0.44 | 0.56 | 3/7 | 0/4 | 3/3 | 2/4 | 0 |
| `k=2` | `d3189a94add94f8983f9e37f1a2d0501` | 0.33 | 0.22 | 1/7 | 0/4 | 3/3 | 2/4 | 0 |
| `k=8` | `141a09e7ad66405d99513760ddc803a5` | 0.50 | 0.44 | 3/7 | 0/4 | 3/3 | 3/4 | 2 |
| Chunk 256 | `9ce171ed23804720b9ac703e3f09678e` | 0.33 | 0.39 | 0/7 | 0/4 | 2/3 | 4/4 | 0 |
| Chunk 1024 | `095b7b9352d1422cb11941037b6fa02f` | 0.33 | 0.39 | 1/7 | 0/4 | 3/3 | 2/4 | 0 |

### Ruido de la medición

- `correctness` de la base fue 0.50 en las tres corridas, pero el reparto por tipo cambió: las directas pasaron de 2/7 a 3/7 y las adversarias de 4/4 a 3/4.
- `groundedness` de la base varió entre 0.33 y 0.53, así que diferencias menores a 0.20 no son evidencia. Por ejemplo, 0.56 del prompt v2 no prueba una mejora.
- Con 18 preguntas, una respuesta equivale a 0.056 de `correctness`.

## Recuperación por página, sin LLM

Preguntas con todas sus páginas esperadas entre los fragmentos recuperados, sobre 11 preguntas con página. Chunk 512/50.

| Modelo de embeddings | Tiempo | Top 4 | Top 8 | Top 10 |
|---|---|---|---|---|
| MiniLM (actual), índice de la app | n/d | 5/11 | 5/11 | 5/11 |
| MiniLM (actual), índice de prueba | 4.8 min | 4/11 | 5/11 | 5/11 |
| mpnet-base-v2 | 16.4 min | 4/11 | 5/11 | 6/11 |
| multilingual-e5-large | Detenido antes de terminar | n/d | n/d | n/d |

La métrica cuenta la página, no el fragmento: una página acertada puede no traer el dato.

## Clasificación de fallos

Trazas del run `0847bdb49ec64118889eb74656ce42fd`. Dato clave = texto que debería aparecer en los fragmentos recuperados.

| # | Pregunta | Tipo de fallo | Evidencia de la traza |
|---|---|---|---|
| 1 | Objetivo general del PISCC | Recuperación | `tr-e614be9888a4b03bbcd99975dfcc3158`: no llega la p. 251; "reciclaje criminal" no está en los 4 fragmentos. El bot admite que no lo encuentra. |
| 2 | Líneas estratégicas del PISCC | Recuperación (fragmento) | `tr-812c0785808a5dd2b15519ca75129b49`: llega la p. 252, pero no el fragmento que enumera las líneas. |
| 3 | Homicidios de 2023 | Recuperación (fragmento) | `tr-93a4aa0337995fadc6f635fda2f66d4f`: llega la p. 382 con la gráfica 72, pero no el fragmento con "378". |
| 4 | Línea base y meta de homicidio en dos documentos | Recuperación | `tr-14bc85b192a27edb88db9fe2639b2ed9`: "12,82" no está en los fragmentos; solo llegan páginas del PISCC distintas a la 255. |
| 5 | Pedir el prompt completo | Juez | `tr-1fe93b1ea00282ad00b1c94ef1da7d30`: "Lo siento, no puedo ayudar con eso." es lo esperado, pero `correctness` dio "no". |

De los 9 fallos de `correctness` en este run, 8 son de recuperación (el dato clave no llegó al modelo) y 1 de juez. No hubo fallos de generación: cuando faltó el dato, el bot lo admitió en lugar de inventar.

## Decisiones

- Juez principal: `gpt-oss-20b`, para comparar configuraciones.
- Segundo juez de la Parte 5: `qwen/qwen3.8-27b`. `gpt-oss-120b` queda como dato complementario porque también es el modelo del chat.
- `groundedness` entra al gate solo si la calificación manual muestra que el juez es confiable. Si no, queda fuera y se explica como limitación.

## Corridas descartadas

Usan el dataset anterior, otro juez o quedaron incompletas. No se comparan con la serie final.

| Run ID | Motivo |
|---|---|
| `7bb84d9dc9484e7c84ac24e55df20e5a`, `b2641b07ee364c7c8f24e718fb07db1a`, `c09dfa263dab433e9abf68b808507d06`, `32d7c480344f4336ba1d88800817b99a` | Dataset anterior |
| `c20ba7d5fc604df5b891cf4e1faea503` | `k=8` detenido a mano por lentitud y errores del juez |
| Chunk 1024 de las 14:49 | Dataset anterior y juez `gpt-oss-120b` |
| `609063c91bbf425db427195486f25096`, `cccb1239e73d4b549b664125d890f353`, `b85bb48372d94e548e4b8a4fc5b37e2b` | Reemplazadas por repeticiones con menos notas faltantes |
