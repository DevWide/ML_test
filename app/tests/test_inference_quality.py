import json
from app.model import analyze_sentiment

def test_inference_quality():
    with open("app/tests/validation_data.json") as f:
        dataset = json.load(f)
    
    for item in dataset:
        result = analyze_sentiment(item["text"])
        assert result[0]["label"] == item["expected_label"]
