from flask import Flask, jsonify, request
from flask_cors import CORS
import os, requests
app = Flask(__name__)
CORS(app)
GROQ_KEY = os.environ.get("GROQ_API_KEY")
@app.route('/api/health')
def health(): return jsonify({"status":"ok","groq": bool(GROQ_KEY)})
@app.route('/api/chat', methods=['POST','GET'])
def chat():
    data = request.get_json(silent=True) or {}
    msg = data.get("message") or request.args.get("message") or "Bonjour"
    if not GROQ_KEY:
        return jsonify({"reply": "Clé GROQ manquante sur Vercel. Ajoute GROQ_API_KEY dans Settings."})
    try:
        r = requests.post("https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {GROQ_KEY}","Content-Type":"application/json"},
            json={"model":"llama-3.3-70b-versatile","messages":[{"role":"system","content":"Tu es Manasse IA, parle français."},{"role":"user","content":msg}]},
            timeout=30)
        return jsonify({"reply": r.json()["choices"][0]["message"]["content"]})
    except Exception as e:
        return jsonify({"reply": f"Erreur Groq: {e}"})
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path): return jsonify({"status":"ok"})
