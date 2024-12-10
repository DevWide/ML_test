import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_predict(client):
    response = client.post("/predict", json={"text": "I love coding!"})
    assert response.status_code == 200
    assert "label" in response.json[0]
    assert response.json[0]["label"] == "positive"
