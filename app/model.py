# Montei esse arquivo para carregar o modelo de análise de sentimentos
from transformers import pipeline

# Carrega o modelo pré-treinado de análise de sentimento
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    # Certifique-se de que o texto está dentro de uma lista
    if isinstance(text, str):
        text = [text]
    return sentiment_model(text)
