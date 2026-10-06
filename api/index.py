from http.server import BaseHTTPRequestHandler
import json, os, urllib.request, urllib.error

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Access-Control-Allow-Methods','GET,POST,OPTIONS')
        self.send_header('Access-Control-Allow-Headers','Content-Type')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        has_key = bool(os.environ.get("GROQ_API_KEY"))
        self.wfile.write(json.dumps({"status":"ok","has_key":has_key,"path":self.path}).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        length = int(self.headers.get('Content-Length',0))
        body = self.rfile.read(length).decode() if length else '{}'
        try:
            data = json.loads(body)
        except:
            data = {}
        msg = data.get("message") or "salut"
        if data.get("messages"):
            try:
                msg = data["messages"][-1].get("content",msg)
            except:
                pass

        key = os.environ.get("GROQ_API_KEY")
        if not key:
            self.wfile.write(json.dumps({"reply":"GROQ_API_KEY manquante"}).encode())
            return
        try:
            req_body = json.dumps({
                "model":"llama-3.1-8b-instant",
                "messages":[{"role":"system","content":"Tu es Manasse IA, parle français, utile et direct."},{"role":"user","content":msg}]
            }).encode()
            req = urllib.request.Request("https://api.groq.com/openai/v1/chat/completions",
                data=req_body,
                headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},
                method="POST")
            with urllib.request.urlopen(req, timeout=30) as resp:
                j = json.loads(resp.read().decode())
            reply = j["choices"][0]["message"]["content"]
            self.wfile.write(json.dumps({"reply":reply}).encode())
        except Exception as e:
            self.wfile.write(json.dumps({"reply":f"Erreur: {e}"}).encode())
