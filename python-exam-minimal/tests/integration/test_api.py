from app.main import app
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)

def test_health_endpoint_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_recommendation_uses_baseline_when_feature_flag_off(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("FEATURE_NEXT_RECOMMENDER", raising=False)
    monkeypatch.delenv("FEATURE_NEXT_RECOMMENDER_ROLLOUT", raising=False)

    response = client.get("/recommendation", params={"user_id": "user-001"})

    assert response.status_code == 200
    assert response.json()["model"] == "baseline-v1"


def test_recommendation_can_use_next_model_when_feature_flag_on(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FEATURE_NEXT_RECOMMENDER", "true")
    monkeypatch.setenv("FEATURE_NEXT_RECOMMENDER_ROLLOUT", "100")

    response = client.get("/recommendation", params={"user_id": "user-002"})

    assert response.status_code == 200
    body = response.json()
    assert body["model"] == "next-v2"
    assert body["user_id"] == "user-002"
