from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/api/health')
def health():
    return jsonify({"status":"ok"})

@app.route('/api/chat', methods=['POST','GET'])
def chat():
    data = request.get_json(silent=True) or {}
    return jsonify({"reply": f"Manasse API OK - reçu: {data.get('message','vide')}"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"info":"API Manasse en ligne", "status":"ok"})
