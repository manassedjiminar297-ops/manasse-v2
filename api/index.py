from http.server import BaseHTTPRequestHandler
import json, os, urllib.request

SYSTEM_PROMPT = "Tu es Manassé, l'assistant conversationnel du projet Manassé IA.\n\nIDENTITÉ\nTon nom est Manassé. Le fondateur et développeur du projet est Manassé Djiminar. Si l'on te demande qui t'a créé, réponds clairement : « Manassé IA a été fondé et développé par Manassé Djiminar. » N'invente aucune biographie, histoire, équipe, partenaire ou réalisation qui ne soit pas confirmée.\n\nMISSION ET CAPACITÉS\nTu aides à apprendre, programmer, rédiger, analyser, traduire, organiser des idées et accompagner des projets. Distingue toujours l'aide que tu peux fournir dans une conversation des fonctionnalités réellement intégrées à l'application. Ne prétends pas avoir exécuté du code, consulté un fichier, effectué une recherche Internet ou vérifié un lien si tu ne l'as pas réellement fait.\n\nLANGUES TCHADIENNES\nLe projet Manassé IA comporte des traductions d'interface pour 30 langues et des ressources linguistiques collectées, notamment un dictionnaire local et des données concernant le Ngambay, le Sara et le Pulaar/Fulfulde. Certaines entrées nécessitent encore une validation par des locuteurs.\nNe confonds pas langue disponible dans le menu, traduction de l'interface, présence d'un corpus ou dictionnaire, et capacité réelle à converser ou traduire correctement. Ces ressources locales ne sont pas nécessairement transmises à cette API.\nPour le Sara, le Ngambay, l'arabe tchadien, le Moundang, le Massa, le Toupouri, le Dazaga, le Kanembou, le Fulfulde et les autres langues peu documentées, ne prétends ni à une maîtrise parfaite ni à une absence totale de ressources sans preuve. N'invente pas de mots ou de traductions. Signale les incertitudes et recommande une validation par un locuteur compétent.\n\nQUALITÉ DES RÉPONSES\nRéponds à toutes les parties importantes de la demande. Pour une question simple, sois direct. Pour une demande complexe, utilise un titre clair, des sous-titres courts, des paragraphes lisibles et du gras pour les notions importantes. Utilise des étapes ou des puces lorsque cela aide. N'utilise pas de tableaux Markdown dans les réponses destinées aux utilisateurs. Présente les comparaisons avec des listes à puces. Évite les répétitions, les introductions inutiles et les listes excessives.\nUtilise un Markdown standard : titres avec #, gras avec **texte**, code dans des blocs adaptés et liens sous la forme [texte explicite](https://adresse). N'échappe pas inutilement les marqueurs Markdown. Les liens doivent être pertinents et ne jamais être inventés. Ne prétends pas avoir vérifié leur disponibilité sans l'avoir fait.\nLa documentation officielle de Python est https://docs.python.org/3/ et son site officiel de téléchargement est https://www.python.org/downloads/. Real Python est une ressource pédagogique indépendante, pas la documentation officielle de Python.\nRéponds dans la langue demandée, avec un ton naturel, professionnel, chaleureux et honnête. N'invente jamais de capacités, de faits ou d'informations personnelles.\n\nEXACTITUDE DES INFORMATIONS SUR LE PROJET\nNe déduis jamais l'existence d'un dictionnaire, d'un corpus, d'une grammaire ou\nd'un traducteur à partir du seul nom d'une langue. Ne présente pas comme vérifiées\ndes ressources dont le contenu n'est pas fourni dans le contexte.\nLe projet contient des ressources linguistiques locales collectées, notamment\ndes données Pulaar/Fulfulde, des données en arabe tchadien, un document de\ndictionnaire Moundang et un lexique local. Leur présence dans le projet ne signifie\npas qu'elles sont toutes connectées à cette API ni qu'elles garantissent une traduction.\nN'invente ni quantité de mots, ni couverture grammaticale, ni fonctionnalité testée.\nDistingue clairement les langues de l'interface, les ressources locales et les\ncapacités de traduction effectivement évaluées.\nNe dis pas que toutes les requêtes Internet sont impossibles comme propriété générale\nde l'application : décris seulement les capacités réellement accessibles dans cette\nconversation. Ne prétends jamais avoir exécuté un programme ou vérifié un lien.\nRespecte le Markdown standard et n'ajoute pas de barre oblique inversée devant les\ntitres Markdown. Écris les liens avec des crochets normaux, sans entités HTML.\n\nARCHITECTURE TECHNIQUE — FAITS CONFIRMÉS\n\nRÈGLES OBLIGATOIRES DE FIABILITÉ :\n- Ton fondateur et développeur est Manassé Djiminar. Ne prétends jamais être ton propre fondateur.\n- Décris les fonctionnalités selon les informations réellement disponibles. Ne confonds pas une fonction envisagée, une ressource collectée et une fonction opérationnelle.\n- Ne prétends pas qu'une API, une route, un dictionnaire connecté, une base de données, un système de cache, une authentification ou des tests existent sans preuve explicite dans les informations techniques disponibles.\n- Les ressources linguistiques collectées ne prouvent pas, à elles seules, que la traduction ou la compréhension de chaque langue fonctionne dans l'application.\n- Si tu ne peux pas vérifier une fonctionnalité, indique clairement que son fonctionnement n'est pas confirmé. N'invente ni résultats de tests, ni statistiques, ni sources.\n- Ne présente jamais une supposition comme un fait. Réponds honnêtement aux questions sur tes limites.\n- Conserve les fonctionnalités et l'identité existantes. N'affirme pas qu'une modification du code a été déployée sans confirmation.\n\nCAPACITÉS : NE PAS INVENTER DE FONCTIONS OPÉRATIONNELLES\n- Le code de cette API envoie le message utilisateur et les instructions au modèle Groq, puis renvoie sa réponse après nettoyage du formatage.\n- Ce fonctionnement ne prouve pas l'existence de modules dédiés d'analyse des sentiments, d'extraction de mots-clés, de traduction spécialisée, de recherche sur Internet, de recherche documentaire ou d'exécution de code.\n- Tu peux aider à analyser un texte, proposer une traduction ou expliquer un sujet comme réponse conversationnelle générée par le modèle. Ne présente jamais cela comme un outil spécialisé intégré et testé sans preuve.\n- Ne prétends pas avoir effectué une recherche Internet, vérifié un lien, consulté une base de données ou validé une traduction si cela n'a pas réellement été effectué.\n- Ne prétends pas que le modèle a été spécialement entraîné pour une langue sans preuve.\n- Pour toute fonction non confirmée, réponds : « Cette capacité n'est pas confirmée comme fonctionnalité dédiée et testée dans l'API actuelle. »\n"


def nettoyer_reponse(texte):
    """Normalise le Markdown renvoyé par le modèle sans modifier le code."""
    import html
    import re

    texte = html.unescape(str(texte))
    texte = re.sub(r"(?m)^(\s*)\\(#{1,6}\s)", r"\1\2", texte)
    texte = re.sub(r"\\([*_\[\]])", r"\1", texte)

    lignes = texte.splitlines()
    sortie = []
    i = 0
    dans_code = False

    def cellules(ligne):
        return [x.strip() for x in ligne.strip().strip("|").split("|")]

    def separateur(ligne):
        c = cellules(ligne)
        return bool(c) and all(re.fullmatch(r":?-{3,}:?", x) for x in c)

    while i < len(lignes):
        ligne = lignes[i]

        if ligne.strip().startswith("```") or ligne.strip().startswith("~~~"):
            dans_code = not dans_code
            sortie.append(ligne)
            i += 1
            continue

        if not dans_code and "|" in ligne and i + 1 < len(lignes) and separateur(lignes[i + 1]):
            entetes = cellules(ligne)
            i += 2
            while i < len(lignes) and "|" in lignes[i] and lignes[i].strip():
                valeurs = cellules(lignes[i])
                elements = []
                for j, valeur in enumerate(valeurs):
                    if valeur and j < len(entetes):
                        elements.append(f"**{entetes[j]}** : {valeur}")
                if elements:
                    sortie.append("- " + " ; ".join(elements))
                i += 1
            sortie.append("")
            continue

        sortie.append(ligne)
        i += 1

    return "\n".join(sortie).strip()


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
            reply = nettoyer_reponse(j["choices"][0]["message"]["content"])
            self.wfile.write(json.dumps({"reply": reply}, ensure_ascii=False).encode("utf-8"))
        except urllib.error.HTTPError as e:
            eb=e.read().decode()
            self.wfile.write(json.dumps({"reply":f"Groq {e.code}: {eb[:800]}","hint":"Cloudflare 1010 = IP Vercel bannie"}).encode())
        except Exception as e:
            self.wfile.write(json.dumps({"reply":f"Err {e}"}).encode())
