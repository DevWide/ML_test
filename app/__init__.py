from flask import Flask, jsonify, request

def create_app():
    """
    Cria e configura a aplicação Flask.
    """
    app = Flask(__name__)

    @app.route('/health', methods=['GET'])
    def health():
        """
        Endpoint de saúde da aplicação.
        Retorna o status 'ok' para indicar que o servidor está funcionando.
        """
        return jsonify({"status": "ok"}), 200

    @app.route('/some-endpoint', methods=['GET'])
    def some_endpoint():
        """
        Um exemplo de endpoint.
        """
        return jsonify({"message": "This is some endpoint"}), 200

    @app.route('/predict', methods=['POST'])
    def predict():
        """
        Endpoint de predição.
        Recebe um JSON com o texto para análise e retorna uma predição simulada.
        """
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Invalid input"}), 400

        prediction = {"label": "positive", "confidence": 0.95}
        return jsonify([prediction]), 200

    return app


app = create_app()
