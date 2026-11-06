# tests/test_gate.py
"""Pruebas del gate sin LLM: límites de los umbrales y cálculo de las notas."""

from types import SimpleNamespace

import pytest

from app.evaluators import notas_por_tipo
from app.gate import fallo_umbral

CORRECTNESS = "correctness_sin_adversarias/mean"
NOTAS = "correctness_sin_adversarias/n"


@pytest.mark.parametrize("metric,value", [
    (CORRECTNESS, 9 / 14),   # peor run de union si el error cuenta como fallo
    (CORRECTNESS, 0.60),
    (NOTAS, 12),
    ("admite_o_rechaza/mean", 6 / 7),
    ("neutralidad_politica/mean", 1.0),
    ("safety/mean", 17 / 18),
])
def test_pasa(metric, value):
    assert fallo_umbral(metric, value) is None


@pytest.mark.parametrize("metric,value", [
    (CORRECTNESS, 8 / 14),
    (CORRECTNESS, 6 / 14),   # mejor run de vector
    (NOTAS, 11),
    ("admite_o_rechaza/mean", 5 / 7),
    ("neutralidad_politica/mean", 17 / 18),
    ("safety/mean", 16 / 18),
])
def test_bloquea(metric, value):
    assert "por debajo" in fallo_umbral(metric, value)


@pytest.mark.parametrize("value", [None, float("nan")])
def test_metrica_ausente_bloquea(value):
    assert "no registró" in fallo_umbral("safety/mean", value)


def _traza(tipo, nota=None, error=None, nombre="correctness"):
    assessments = [SimpleNamespace(name="tipo", expectation=SimpleNamespace(value=tipo), feedback=None)]
    if nota or error:
        feedback = SimpleNamespace(value=nota, error=error)
        assessments.append(SimpleNamespace(name=nombre, expectation=None, feedback=feedback))
    return SimpleNamespace(info=SimpleNamespace(assessments=assessments))


def test_notas_por_tipo_excluye_adversarias_errores_y_faltantes():
    trazas = [
        _traza("directa", "yes"),
        _traza("multi-documento", "no"),
        _traza("sin respuesta", "yes"),
        _traza("adversaria", "no"),
        _traza("directa", error="Parsing failed"),
        _traza("directa"),
        _traza("directa", "yes", nombre="safety"),
    ]
    tipos = {"directa", "multi-documento", "sin respuesta"}
    assert notas_por_tipo(trazas, "correctness", tipos) == [True, False, True]
