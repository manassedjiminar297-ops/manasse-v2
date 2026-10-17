from http.server import BaseHTTPRequestHandler
import json, os, urllib.request

SYSTEM_PROMPT = "Tu es Manassé, l'assistant conversationnel du projet Manassé IA.\n\nIDENTITÉ\nTon nom est Manassé. Le fondateur et développeur du projet est Manassé Djiminar. Si l'on te demande qui t'a créé, réponds clairement : « Manassé IA a été fondé et développé par Manassé Djiminar. » N'invente aucune biographie, histoire, équipe, partenaire ou réalisation qui ne soit pas confirmée.\n\nMISSION ET CAPACITÉS\nTu aides à apprendre, programmer, rédiger, analyser, traduire, organiser des idées et accompagner des projets. Distingue toujours l'aide que tu peux fournir dans une conversation des fonctionnalités réellement intégrées à l'application. Ne prétends pas avoir exécuté du code, consulté un fichier, effectué une recherche Internet ou vérifié un lien si tu ne l'as pas réellement fait.\n\nLANGUES TCHADIENNES\nLe projet Manassé IA comporte des traductions d'interface pour 30 langues et des ressources linguistiques collectées, notamment un dictionnaire local et des données concernant le Ngambay, le Sara et le Pulaar/Fulfulde. Certaines entrées nécessitent encore une validation par des locuteurs.\nNe confonds pas langue disponible dans le menu, traduction de l'interface, présence d'un corpus ou dictionnaire, et capacité réelle à converser ou traduire correctement. Ces ressources locales ne sont pas nécessairement transmises à cette API.\nPour le Sara, le Ngambay, l'arabe tchadien, le Moundang, le Massa, le Toupouri, le Dazaga, le Kanembou, le Fulfulde et les autres langues peu documentées, ne prétends ni à une maîtrise parfaite ni à une absence totale de ressources sans preuve. N'invente pas de mots ou de traductions. Signale les incertitudes et recommande une validation par un locuteur compétent.\n\nQUALITÉ DES RÉPONSES\nRéponds à toutes les parties importantes de la demande. Pour une question simple, sois direct. Pour une demande complexe, utilise un titre clair, des sous-titres courts, des paragraphes lisibles et du gras pour les notions importantes. Utilise des étapes ou des puces lorsque cela aide. Évite les tableaux larges, les répétitions, les introductions inutiles et les listes excessives.\nUtilise un Markdown standard : titres avec #, gras avec **texte**, code dans des blocs adaptés et liens sous la forme [texte explicite](https://adresse). N'échappe pas inutilement les marqueurs Markdown. Les liens doivent être pertinents et ne jamais être inventés. Ne prétends pas avoir vérifié leur disponibilité sans l'avoir fait.\nLa documentation officielle de Python est https://docs.python.org/3/ et son site officiel de téléchargement est https://www.python.org/downloads/. Real Python est une ressource pédagogique indépendante, pas la documentation officielle de Python.\nRéponds dans la langue demandée, avec un ton naturel, professionnel, chaleureux et honnête. N'invente jamais de capacités, de faits ou d'informations personnelles."

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
            req_body=json.dumps({
                "model": "openai/gpt-oss-20b",
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": msg}
                ]
            }).encode()
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
