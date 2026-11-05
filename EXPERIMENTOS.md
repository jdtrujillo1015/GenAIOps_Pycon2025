# Bitácora de experimentos

Evidencia para `INFORME.md`. Los puntajes de jueces parciales no se comparan con los de evaluaciones completas.

| Fecha | Run ID | Prompt | k | Chunk / overlap | Dataset | Juez | correctness | retrieval_groundedness | Nota |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-05 | `7bb84d9dc9484e7c84ac24e55df20e5a` | v1 | 4 | 512 / 50 | 18 preguntas | `groq:/openai/gpt-oss-20b` | 0.44 | 0.41 (1 de 18 falló) | Línea base con 2 jueces |

## Línea base: correctness por tipo

| Tipo | Correctas |
|---|---|
| Directa | 3 de 7 |
| Multi-documento | 0 de 4 |
| Sin respuesta | 3 de 3 |
| Adversaria | 2 de 4 |

Hipótesis por revisar en las trazas (Parte 3):
- Varias directas y multi-documento responden que el dato no está en los fragmentos: posible fallo de recuperación.
- `retrieval_groundedness` marca "no" en respuestas correctas sin datos, como negativas y "no tengo información": posible fallo de juez.
- Dos negativas adversarias salen incorrectas porque la respuesta esperada también pide redirigir: posible fallo de dataset.
