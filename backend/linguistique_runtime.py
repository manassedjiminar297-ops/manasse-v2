# -*- coding: utf-8 -*-
"""Contexte lexical local pour Manassé IA."""
import json


def _selection_lexicale(donnees, question):
    import unicodedata
    def mots(texte):
        texte = unicodedata.normalize("NFD", str(texte).casefold())
        texte = "".join(c for c in texte if not unicodedata.combining(c))
        texte = "".join(c if c.isalpha() else " " for c in texte)
        stop = {"les", "des", "une", "dans", "pour", "avec", "comment",
                "est", "que", "qui", "veux", "peux", "moi"}
        return {m for m in texte.split() if len(m) > 2 and m not in stop}

    question_mots = mots(question)
    scores = []
    for cle, entree in donnees.get("entrees", {}).items():
        if not isinstance(entree, dict):
            continue
        texte = " ".join(str(entree.get(k, "")) for k in
                         ("forme", "sens_francais", "note", "exemple"))
        score = len(question_mots & mots(texte))
        if score:
            scores.append((score, cle, entree))
    scores.sort(key=lambda x: x[0], reverse=True)
    resultat = dict(donnees)
    resultat["entrees"] = {cle: entree for _, cle, entree in scores[:4]}
    resultat["selection"] = (
        "Correspondances lexicales indicatives, pas traduction validée."
        if scores else "Aucune entrée pertinente trouvée par ce filtre."
    )
    return resultat

def contexte_linguistique(code_langue, conversation=""):
    try:
        from lexique_local import LEXIQUE_LOCAL_VERIFIE, SOURCES
    except Exception:
        return ""

    code = str(code_langue or "").strip().lower()
    ALIASES_LANGUES = {
    "sba": "ngambay",
    "sara": "sar",
    "sar": "sar",
    "ngambaye": "ngambay",
    "ngambay": "ngambay",
}
    cle = ALIASES_LANGUES.get(code, code)
    donnees = LEXIQUE_LOCAL_VERIFIE.get(cle)
    if not donnees:
        return ""

    contexte = (
        "\n\nRESSOURCE LEXICALE LOCALE — référence, pas traduction garantie :\n"
        "Ces références locales ne garantissent pas une traduction complète. Une entrée attestée dans un dictionnaire n'est pas nécessairement validée par un locuteur. Ne présente pas une phrase composée à partir de quelques mots comme une traduction vérifiée. Si la sélection est vide, indique qu'aucune référence locale pertinente n'a été trouvée. Si la demande vise une traduction ou une formulation dans cette langue et qu'aucune entrée pertinente n'est trouvée, ne réponds pas au sujet sous-jacent et ne propose aucune traduction ; signale brièvement l'absence de référence locale, puis demande si la personne souhaite une explication en français. Distingue les références fournies des formulations que tu proposes. Respecte les champs statut, validation_locuteur et les notes "
        "et leur contexte. N'invente pas de vocabulaire manquant. Si une forme est "
        "incertaine, indique-le. Le lexique Sar ne représente pas automatiquement "
        "toutes les variétés Sara.\n"
        + json.dumps(_selection_lexicale(donnees, conversation), ensure_ascii=False, default=str)
    )
    source = SOURCES.get(cle) if isinstance(SOURCES, dict) else None
    if source:
        contexte += "\nSource du lexique : " + str(source)
    return contexte
