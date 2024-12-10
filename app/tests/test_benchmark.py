import time
from app import app  
from app.model import analyze_sentiment

def test_prediction_time():
    start_time = time.time()
    analyze_sentiment("This is a test")
    end_time = time.time()
    assert (end_time - start_time) < 0.5, "Prediction took too long"  

def test_performance():
    client = app.test_client()

    start = time.time()
    response = client.post("/predict", json={"text": "I love coding!"})
    end = time.time()

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert (end - start) < 1.0, "API response took too long"  
    print(f"Response time: {end - start:.4f} seconds")
