from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/health')
def health():
    return jsonify({"status": "ok", "message": "Manasse fonctionne"})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    msg = data.get('message', 'Salut')
    return jsonify({"reply": f"Echo: {msg} - backend ok, ajoute GEMINI_API_KEY dans Vercel Settings"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"info": "API Manasse en ligne. Utilise /api/health et /api/chat"})
