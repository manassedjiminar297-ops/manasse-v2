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
    if GROQ_KEY:
        try:
            r = requests.post("https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {GROQ_KEY}","Content-Type":"application/json"},
                json={"model":"llama-3.3-70b-versatile","messages":[{"role":"system","content":"Tu es Manasse IA, assistant utile qui parle francais, tchadien."},{"role":"user","content":msg}]},
                timeout=30)
            txt = r.json()["choices"][0]["message"]["content"]
            return jsonify({"reply": txt})
        except Exception as e:
            return jsonify({"reply": f"Erreur Groq: {e} | Message: {msg}"})
    return jsonify({"reply": f"Manasse (sans cle): {msg}"})
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path): return jsonify({"info":"API Manasse avec Groq","status":"ok"})
