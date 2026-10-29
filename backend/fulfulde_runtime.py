
from pathlib import Path
from functools import lru_cache
import json
import re
import unicodedata

BASE = Path(__file__).resolve().parent / "donnees_linguistiques" / "fulfulde_fuuta_tooro"
STOP = {
    "les", "des", "une", "un", "le", "la", "de", "du", "et", "en", "pour",
    "avec", "sur", "dans", "est", "sont", "qui", "que", "comment", "quoi",
    "je", "tu", "il", "elle", "vous", "nous", "mon", "ma", "mes", "au", "aux",
    "ce", "cette", "ces", "the", "and", "for", "are", "you", "your"
}

def _normaliser(s):
    s = unicodedata.normalize("NFKD", str(s).casefold())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^\w\sɓɗƴŋ]", " ", s)).strip()

def _mots(s):
    return {m for m in _normaliser(s).split()
            if len(m) >= 3 and m not in STOP}

def _lire_jsonl(path):
    resultat = []
    try:
        for ligne in path.read_text(encoding="utf-8-sig").splitlines():
            try:
                item = json.loads(ligne)
                if isinstance(item, dict):
                    resultat.append(item)
            except Exception:
                pass
    except Exception:
        pass
    return resultat

def _premier(d, cles):
    for cle in cles:
        val = d.get(cle)
        if isinstance(val, str) and val.strip():
            return val.strip()
    return ""

@lru_cache(maxsize=1)
def _charger():
    lignes = []
    fichier = BASE / "lexique_pulaar.json"
    try:
        data = json.loads(fichier.read_text(encoding="utf-8-sig"))
        for e in data.get("entrees", []):
            fr, ff = e.get("sens", ""), e.get("mot", "")
            if fr and ff:
                lignes.append({
                    "fr": str(fr), "ff": str(ff),
                    "theme": "lexique", "type": "lexique"
                })
    except Exception:
        pass

    for fichier in sorted(BASE.glob("*.jsonl")):
        for e in _lire_jsonl(fichier):
            fr = _premier(e, (
                "francais", "français", "fr", "french",
                "terme_francais", "definition_francaise", "sens"
            ))
            ff = _premier(e, (
                "pulaar", "terme_pulaar", "mot_pulaar",
                "fulfulde_texte", "ff", "fub", "target", "cible",
                "traduction"
            ))
            if not ff:
                variante = str(e.get("fulfulde", "")).strip().casefold()
                if variante not in {"fuuta-tooro", "maasina", "macina"}:
                    ff = _premier(e, ("fulfulde",))
            if fr and ff:
                lignes.append({
                    "fr": str(fr), "ff": str(ff),
                    "theme": str(e.get("theme", fichier.stem)),
                    "type": fichier.stem
                })

    resultat, vus = [], set()
    for ligne in lignes:
        cle = (ligne["fr"], ligne["ff"])
        if cle not in vus:
            vus.add(cle)
            resultat.append(ligne)
    return resultat

def contexte_fulfulde(code_langue, conversation=""):
    code = str(code_langue or "").strip().casefold().replace("-", "_")
    alias = {
        "pulaar": "ff",
        "fuc": "ff",
        "ff_latn": "ff",
        "fub": "ff",
        "fulani": "ff",
    }
    code = alias.get(code, code)
    if code not in {"ff", "fulfulde"}:
        return ""

    lignes = _charger()
    if not lignes:
        return ""

    question = str(conversation)[-1800:]
    mots_q = _mots(question)
    scores = []
    for ligne in lignes:
        mots_fr = _mots(ligne["fr"])
        mots_ff = _mots(ligne["ff"])
        score = 2 * len(mots_q & mots_fr) + len(mots_q & mots_ff)
        if score:
            scores.append((score, ligne))

    if scores:
        scores.sort(key=lambda x: x[0], reverse=True)
        choisis = [ligne for _, ligne in scores[:3]]
    else:
        choisis = [
            ligne for ligne in lignes
            if ligne["type"] == "dialogues_pulaar"
            and any(m in (ligne["theme"] + " " + ligne["fr"]).casefold()
                    for m in ("salutation", "bonjour", "présentation"))
        ][:2]
        if not choisis:
            choisis = [
                ligne for ligne in lignes
                if ligne["type"] == "dialogues_pulaar"
            ][:2]
        if not choisis:
            choisis = lignes[:2]

    contexte = [
        "[RÉFÉRENCE LINGUISTIQUE FULFULDE — VARIANTE IDENTIFIÉE]",
        "Source : J'apprends le Pulaar — méthode audio-orale Fuuta-Tooro.",
        "Licence des données : CC BY 4.0. Attribution : Muttaar, "
        "https://huggingface.co/datasets/ARPRIM/Pulaar_Fulfulde",
        "La variante documentée est principalement Fuuta-Tooro "
        "(Mauritanie/Sénégal), et non une garantie de Fulfulde tchadien.",
        "Utilise les correspondances suivantes comme références lexicales, "
        "pas comme preuves que tous les dialectes sont identiques. "
        "Si une formulation propre au Tchad n'est pas vérifiable, "
        "sois transparent et ne l'invente pas.",
        "Correspondances disponibles :"
    ]
    for ligne in choisis:
        fr = ligne["fr"].replace("\n", " ")[:180]
        ff = ligne["ff"].replace("\n", " ")[:180]
        contexte.append(f"- Français : {fr} → Pulaar/Fulfulde Fuuta-Tooro : {ff}")
    return "\n" + "\n".join(contexte) + "\n"
