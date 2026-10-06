from app.main import create_app


def test_home_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "InternCareerPath CI/CD Pipeline"
    assert data["status"] == "running"


def test_health_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 500
    assert response.get_json() == {"status": "healthy"}
