import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test del endpoint principal"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "DevSecOps Enterprise Lab"
    assert data["status"] == "running"


def test_health_endpoint(client):
    """Test del health check"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_get_users(client):
    """Test del endpoint de usuarios GET"""
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    data = response.get_json()
    assert "users" in data
    assert len(data["users"]) == 3


def test_create_user(client):
    """Test del endpoint de usuarios POST"""
    response = client.post("/api/v1/users", json={"name": "David"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "David"
    assert "id" in data


def test_create_user_missing_name(client):
    """Test del endpoint de usuarios POST sin nombre"""
    response = client.post("/api/v1/users", json={})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Name is required"
