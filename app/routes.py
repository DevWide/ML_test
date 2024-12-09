# Definição das rotas da API

from flask import request, jsonify
from app.model import analyze_sentiment

def configure_routes(app):
    @app.route("/predict", methods=["POST"])
    def predict():
        data = request.json
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400
        return jsonify(analyze_sentiment(text))
    
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200