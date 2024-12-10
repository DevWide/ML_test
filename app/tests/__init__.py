from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/some-endpoint', methods=['GET'])
def some_endpoint():
    return jsonify({"message": "This is some endpoint"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"prediction": f"Received: {data['text']}"}), 200
