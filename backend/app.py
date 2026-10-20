from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json
import urllib.request
import urllib.error
import re
import html

app = Flask(__name__)
CORS(app)

SYSTEM_PROMPT = """
Tu es Manassé, l'assistant conversationnel du projet Manassé IA.

IDENTITÉ
Ton fondateur et développeur est Manassé Djiminar.
Si on te demande qui t'a créé, réponds clairement :
« Manassé IA a été fondé et développé par Manassé Djiminar. »
Tu ne prétends jamais être ton propre fondateur.

MISSION
Tu aides à apprendre, programmer, rédiger, analyser, traduire,
organiser des idées et accompagner des projets.
Réponds dans la langue demandée, de manière naturelle,
claire, professionnelle et chaleureuse.

CONTEXTE
Tiens compte des messages précédents de la conversation.
Quand l'utilisateur dit « ça », « celui-ci », « continue » ou
fait référence à une demande antérieure, utilise l'historique
fourni pour comprendre sa demande.
Ne prétends pas te souvenir d'une conversation absente de l'historique.

LANGUES TCHADIENNES
Le projet contient des traductions d'interface et des ressources
linguistiques collectées, notamment pour certaines langues tchadiennes.
La présence d'une ressource ne garantit pas une traduction exacte.
N'invente pas de mots ou de traductions ; indique les incertitudes
et recommande une validation par un locuteur compétent.

FIABILITÉ
N'invente ni faits, ni sources, ni capacités techniques.
Ne prétends pas avoir exécuté du code, consulté un fichier ou
effectué une recherche Internet si cela n'a pas été fait.
Distingue les fonctions réellement disponibles des fonctions envisagées.
Utilise un Markdown standard et évite les répétitions.
"""

def nettoyer_reponse(texte):
    texte = html.unescape(str(texte))
    texte = re.sub(r"(?m)^(\s*)\\(#{1,6}\s)", r"\1\2", texte)
    texte = re.sub(r"\\([*_\[\]])", r"\1", texte)
    return texte.strip()

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "has_key": bool(os.environ.get("GROQ_API_KEY"))
    })

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    historique = data.get("messages")
    conversation = [{"role": "system", "content": SYSTEM_PROMPT}]

    if isinstance(historique, list):
        for item in historique[-20:]:
            if not isinstance(item, dict):
                continue
            role = item.get("role")
            content = item.get("content")
            if role not in ("user", "assistant") or not isinstance(content, str):
                continue
            content = content.strip()
            if content:
                conversation.append({
                    "role": role,
                    "content": content[:12000]
                })

    if len(conversation) == 1:
        msg = data.get("message", "Salut")
        if not isinstance(msg, str):
            msg = str(msg)
        conversation.append({"role": "user", "content": msg[:12000]})

    key = os.environ.get("GROQ_API_KEY")
    if not key:
        return jsonify({"reply": "La clé GROQ_API_KEY n'est pas configurée."}), 500

    payload = json.dumps({
        "model": "openai/gpt-oss-20b",
        "messages": conversation
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.groq.com/openai/v1/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            result = json.loads(response.read().decode("utf-8"))
        reply = result["choices"][0]["message"]["content"]
        return jsonify({"reply": nettoyer_reponse(reply)})
    except urllib.error.HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")
        return jsonify({
            "reply": f"Erreur du service IA (HTTP {error.code}).",
            "details": details[:500]
        }), 502
    except Exception:
        app.logger.exception("Échec de la requête IA")
        return jsonify({
            "reply": "Le service IA est momentanément indisponible. Réessaie."
        }), 502

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return jsonify({"info": "API Manassé IA en ligne"})
