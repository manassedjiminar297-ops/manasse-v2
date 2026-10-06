from flask import Flask, jsonify, request
import os

# Lazy import requests pour éviter crash au démarrage si manquant
app = Flask(__name__)

@app.after_request
def after(r):
    r.headers.add('Access-Control-Allow-Origin','*')
    r.headers.add('Access-Control-Allow-Headers','Content-Type')
    r.headers.add('Access-Control-Allow-Methods','GET,POST,OPTIONS')
    return r

@app.route('/api/health')
def health():
    return jsonify({"status":"ok","has_key": bool(os.environ.get("GROQ_API_KEY"))})

@app.route('/api/chat', methods=['POST','GET','OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return jsonify({"ok":True})
    try:
        import requests
    except Exception as e:
        return jsonify({"reply": f"Module requests manquant: {e}"}), 500

    data = request.get_json(silent=True) or {}
    msg = data.get("message")
    if not msg and data.get("messages"):
        try:
            msg = data["messages"][-1].get("content","")
        except:
            pass
    msg = msg or request.args.get("message") or "Salut"

    key = os.environ.get("GROQ_API_KEY")
    if not key:
        return jsonify({"reply":"GROQ_API_KEY manquante sur Vercel"}), 500

    try:
        r = requests.post("https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}","Content-Type":"application/json"},
            json={"model":"llama-3.1-8b-instant","messages":[{"role":"system","content":"Tu es Manasse IA, parle français."},{"role":"user","content":msg}]},
            timeout=30)
        j = r.json()
        if "error" in j:
            return jsonify({"reply": f"Groq error: {j['error']}"}), 500
        return jsonify({"reply": j["choices"][0]["message"]["content"]})
    except Exception as e:
        return jsonify({"reply": f"Exception: {e}"}), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"status":"live"})

# Vercel doit trouver app
