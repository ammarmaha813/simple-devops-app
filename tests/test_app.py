import os
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app


client = TestClient(app)


def test_home_status_code():
    """L'endpoint racine doit répondre avec le code HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_home_response_contains_expected_fields():
    """La réponse de / doit contenir message, hostname, time et port."""
    response = client.get("/")
    assert response.status_code == 200

    payload = response.json()
    assert "message" in payload
    assert "hostname" in payload
    assert "time" in payload
    assert "port" in payload


def test_health_endpoint_returns_healthy():
    """L'endpoint /health doit renvoyer status healthy et HTTP 200."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_users_returns_exactly_two_users():
    """L'endpoint /users doit renvoyer exactement deux utilisateurs."""
    response = client.get("/users")
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert len(users) == 2

    for user in users:
        assert "id" in user
        assert "name" in user


def test_metrics_endpoint_status_code():
    """L'endpoint /metrics doit répondre avec le code HTTP 200."""
    response = client.get("/metrics")
    assert response.status_code == 200


def test_metrics_endpoint_contains_app_requests_total():
    """La réponse /metrics doit contenir la métrique Prometheus app_requests_total."""
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "app_requests_total" in response.text
