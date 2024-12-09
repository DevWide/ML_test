import time
from app.model import analyze_sentiment
from app import create_app

def test_prediction_time():
    start_time = time.time()
    analyze_sentiment("This is a test")
    end_time = time.time()
    assert (end_time - start_time) < 0.5  # 500ms máximo

def test_performance():
    client = app.test_client()
    start = time.time()
    response = client.post("/predict", json={"text": "I love coding!"})
    end = time.time()

    assert response.status_code == 200
    assert (end - start) < 0.5 
