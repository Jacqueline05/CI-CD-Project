import json

from app import app


def test_home_returns_service_details():
    response = app.test_client().get("/")

    assert response.status_code == 200
    body = json.loads(response.data)
    assert body["service"] == "CI/CD Demo Application"
    assert body["status"] == "running"


def test_health_endpoint_is_healthy():
    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
