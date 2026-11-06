# tests/test_run_eval.py
"""
Quality gate: la última evaluación (python app/run_eval.py) debe superar
los umbrales de app/gate.py.
"""

import mlflow
import pytest

from app.gate import THRESHOLDS, fallo_umbral

EVAL_EXPERIMENT = "rag_evaluation"


@pytest.fixture(scope="module")
def latest_eval_run():
    experiment = mlflow.get_experiment_by_name(EVAL_EXPERIMENT)
    if experiment is None:
        pytest.skip("No hay evaluaciones. Ejecuta primero: python app/run_eval.py")
    runs = mlflow.search_runs(experiment_ids=[experiment.experiment_id],
                              order_by=["start_time DESC"], max_results=1)
    if runs.empty:
        pytest.skip("El experimento de evaluación no tiene ejecuciones")
    return runs.iloc[0]


@pytest.mark.parametrize("metric", THRESHOLDS)
def test_umbral_minimo(latest_eval_run, metric):
    value = latest_eval_run.get(f"metrics.{metric}")
    print(f"{metric} = {value} (mínimo {THRESHOLDS[metric]})")
    motivo = fallo_umbral(metric, value)
    assert motivo is None, motivo
