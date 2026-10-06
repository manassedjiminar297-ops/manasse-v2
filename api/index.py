from flask import Flask, jsonify, request
from flask_cors import CORS
import os, requests
app = Flask(__name__)
CORS(app)
GROQ_KEY = os.environ.get("GROQ_API_KEY")

@app.route('/api/health')
def health():
    return jsonify({"status":"ok","groq": bool(GROQ_KEY), "key_len": len(GROQ_KEY) if GROQ_KEY else 0})

@app.route('/api/chat', methods=['POST','GET','OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return jsonify({"ok":True})
    data = request.get_json(silent=True) or {}
    # Supporte les 2 formats: {message: "..."} et {messages: [{content}]}
    msg = data.get("message")
    if not msg and "messages" in data:
        try:
            msg = data["messages"][-1].get("content", "")
        except:
            msg = ""
    msg = msg or request.args.get("message") or "Bonjour"

    if not GROQ_KEY:
        return jsonify({"reply": "Clé GROQ manquante. Va dans Vercel > Settings > Environment Variables > ajoute GROQ_API_KEY"}), 500
    try:
        r = requests.post("https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {GROQ_KEY}","Content-Type":"application/json"},
            json={"model":"llama-3.1-8b-instant","messages":[{"role":"system","content":"Tu es Manasse IA, assistant qui parle français, amical et utile."},{"role":"user","content":msg}]},
            timeout=30)
        j = r.json()
        if "choices" not in j:
            return jsonify({"reply": f"Erreur Groq: {j}"}), 500
        return jsonify({"reply": j["choices"][0]["message"]["content"]})
    except Exception as e:
        return jsonify({"reply": f"Erreur: {e}"}), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"status":"ok", "groq_configured": bool(GROQ_KEY)})
