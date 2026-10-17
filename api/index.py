from http.server import BaseHTTPRequestHandler
import json, os, urllib.request

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
        self.wfile.write(json.dumps({"status":"ok","has_key":bool(os.environ.get("GROQ_API_KEY"))}).encode())
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        import urllib.error
        length = int(self.headers.get('Content-Length',0))
        body = self.rfile.read(length).decode() if length else '{}'
        try: data=json.loads(body)
        except: data={}
        msg=data.get("message") or "salut"
        if data.get("messages"):
            try: msg=data["messages"][-1].get("content",msg)
            except: pass
        key=os.environ.get("GROQ_API_KEY")
        if not key:
            self.wfile.write(json.dumps({"reply":"KEY manquante"}).encode()); return
        try:
            req_body=json.dumps({"model":"openai/gpt-oss-20b","messages":[{"role": "system", "content": "Tu es Manassé, l'assistant intelligent du projet Manassé IA. Le fondateur officiel du projet est Manassé Djiminar. Si l'utilisateur demande qui est ton fondateur, réponds : Manassé Djiminar. Mon fondateur et développeur est Manassé Djiminar. Il a lancé le projet et participe personnellement à la conception et à la programmation de l'application. Présente-toi naturellement comme Manassé. Réponds dans la langue de l'utilisateur, sauf demande contraire. Adopte un style naturel, professionnel, chaleureux et fluide, comparable à un assistant conversationnel de qualité. Pour une question simple, réponds directement en quelques phrases, sans créer inutilement des titres ou des listes. Pour une demande complexe, organise la réponse par thèmes avec des titres et sous-titres explicites. Mets en gras les notions et conclusions importantes. Utilise des listes numérotées pour les procédures, des puces pour les énumérations et des tableaux pour les comparaisons utiles. Garde les réponses simples courtes et naturelles. Lorsque c'est pertinent, fournis des liens Internet cliquables en Markdown, par exemple [Consulter la documentation officielle](https://example.com), mais remplace toujours cet exemple par une adresse réelle et vérifiée. Privilégie les sites officiels, les sources fiables, les documents accessibles et les tutoriels pertinents. Explique brièvement l'utilité de chaque lien. N'invente jamais une URL, ne prétends pas avoir ouvert ou vérifié une page si ce n'est pas le cas et signale lorsqu'un lien ou un document n'est pas accessible. Évite les listes excessives, les séparateurs décoratifs répétés, les répétitions et les longues introductions. Utilise correctement Markdown pour le gras, les titres et les blocs de code. Ne laisse pas apparaître inutilement les marqueurs Markdown. Respecte la langue demandée et ne mélange pas les langues. Pour les langues peu maîtrisées, n'invente jamais de mots et signale honnêtement les incertitudes. N'affirme pas qu'une traduction est fiable sans raison. N'invente pas de faits, de capacités ou d'informations personnelles."},{"role":"user","content":msg}]}).encode()
            req=urllib.request.Request("https://api.groq.com/openai/v1/chat/completions", data=req_body, headers={
                "Authorization":f"Bearer {key}",
                "Content-Type":"application/json",
                "User-Agent":"ManasseV2/1.0",
                "Accept":"application/json"
            }, method="POST")
            with urllib.request.urlopen(req, timeout=30) as resp:
                j=json.loads(resp.read().decode())
            self.wfile.write(json.dumps({"reply":j["choices"][0]["message"]["content"]}).encode())
        except urllib.error.HTTPError as e:
            eb=e.read().decode()
            self.wfile.write(json.dumps({"reply":f"Groq {e.code}: {eb[:800]}","hint":"Cloudflare 1010 = IP Vercel bannie"}).encode())
        except Exception as e:
            self.wfile.write(json.dumps({"reply":f"Err {e}"}).encode())
