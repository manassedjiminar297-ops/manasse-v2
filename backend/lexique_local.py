# -*- coding: utf-8 -*-
"""
Lexique local de Manassé IA.

Les expressions sont accompagnées de leurs sources et de leur statut.
Ce fichier est indépendant de translations.py.
Les entrées attestées dans un dictionnaire doivent encore être validées
par un locuteur avant leur intégration définitive dans l'interface.
"""

VERSION_LEXIQUE = "1.0"

SOURCES = {
    "ngambay": {
        "titre": "Petit Dictionnaire de la Langue Ngambay",
        "auteurs": [
            "Nangone Jacob Chata",
            "Simeon Mbayrem Djimadoum",
            "John M. Keegan",
        ],
        "edition": "Cinquième édition, mai 2015",
        "url": (
            "https://morkegbooks.com/Services/World/Languages/"
            "SaraBagirmi/SoundDictionary/Ngambay/"
        ),
    },
    "sar": {
        "titre": "Dictionnaire Sar",
        "auteurs": ["Gotengaye Constant", "John M. Keegan"],
        "edition": "Première édition, mars 2016",
        "url": (
            "https://morkegbooks.com/Services/World/Languages/"
            "SaraBagirmi/SoundDictionary/Sar/"
        ),
    },
}

LEXIQUE_LOCAL_VERIFIE = {
    "ngambay": {
        "nom": "Ngambay",
        "etat_general": "Documentation trouvée ; validation locale nécessaire.",
        "entrees": {
            "greeting": {
                "forme": "Lápíyà lə̀-í.",
                "sens_francais": "Salut à toi.",
                "statut": "Attesté dans le dictionnaire",
                "validation_locuteur": "À effectuer",
                "source_url": "https://morkegbooks.com/Services/World/Languages/SaraBagirmi/SoundDictionary/Ngambay/Ngmb2566.htm",
                "exemple": "òý-yō, lápíyà yàá. — Oui, salut bien.",
            },
            "salutation_courte": {
                "forme": "Lápíyà",
                "sens_francais": "Salutation ; salut.",
                "statut": "Attesté dans le dictionnaire",
                "validation_locuteur": "À effectuer",
                "source_url": "https://morkegbooks.com/Services/World/Languages/SaraBagirmi/SoundDictionary/Ngambay/Ngmb2566.htm",
                "exemple": "Lápíyà lə̀-í. — Salut à toi.",
            },
            "study": {
                "forme": "ndó",
                "sens_francais": "Apprendre ; étudier ; enseigner selon le contexte.",
                "statut": "Sens lexical documenté",
                "validation_locuteur": "À effectuer avant usage comme libellé UI",
            },
            "goodbye_person_who_leaves": {
                "forme": "āw dɨ̀ màjé.",
                "sens_francais": "Au revoir, à la personne qui part.",
                "note": "Sens littéral indiqué par le dictionnaire : va bien.",
                "statut": "Attesté dans le dictionnaire",
                "validation_locuteur": "À effectuer",
            },
            "goodbye_person_who_stays": {
                "forme": "ísī dɨ̀ màjé.",
                "sens_francais": "Au revoir, à la personne qui reste.",
                "note": "Sens littéral indiqué par le dictionnaire : reste bien.",
                "statut": "Attesté dans le dictionnaire",
                "validation_locuteur": "À effectuer",
            },
        },
    },

    "sar": {
        "nom": "Sar",
        "etat_general": (
            "Dictionnaire identifié ; équivalents destinés à l'interface "
            "non encore vérifiés."
        ),
        "entrees": {
            "thanks": {
                "forme": "kɨ́rà",
                "sens_francais": "Remerciements",
                "exemple": "m̄-rā-ī kɨ́rà ngá̰y.",
                "traduction_exemple": "Je te remercie beaucoup.",
                "note": (
                    "Le dictionnaire donne aussi la phrase "
                    "m̄-rā-ī kɨ́rà ngá̰y : "
                    "Je te remercie beaucoup."
                ),
                "statut": "Documenté dans le dictionnaire Sar",
                "validation_locuteur": "À effectuer",
                "source_url": (
                    "https://morkegbooks.com/Services/World/"
                    "Languages/SaraBagirmi/pdfs/Sar.pdf"
                ),
            },
            "understand": {
                "forme": "gèᶉ̄ kùm",
                "sens_francais": "Comprendre le sens",
                "statut": "Documenté dans le dictionnaire Sar",
                "validation_locuteur": "À effectuer",
                "source_url": (
                    "https://morkegbooks.com/Services/World/"
                    "Languages/SaraBagirmi/pdfs/Sar.pdf"
                ),
            },
        },
    },
}

# Notions à rechercher pour les prochaines traductions.
CONCEPTS_A_TRADUIRE = {
    "ngambay": [
        "merci",
        "lire",
        "écrire",
        "comprendre",
        "expliquer",
        "créer",
        "analyser",
        "paramètres",
        "profil",
        "annuler",
        "envoyer",
    ],
    "sar": [
        "salutation",
        "merci",
        "étudier",
        "apprendre",
        "lire",
        "écrire",
        "comprendre",
        "expliquer",
        "créer",
        "analyser",
        "paramètres",
        "profil",
        "annuler",
        "envoyer",
    ],
}




# MANASSE_NGAMBAY_ENTREES_COMPLEMENTAIRES_2026_10
# Source : Petit Dictionnaire de la Langue Ngambay,
# Morkeg Books, cinquième édition, mai 2015.
# Les constructions doivent être validées par un locuteur.

LEXIQUE_LOCAL_VERIFIE.setdefault("ngambay", {}).setdefault(
    "entrees", {}
).update({
    "help": {
        "forme": "lá",
        "sens_francais": "Aider quelqu'un",
        "exemple": "ī-tā bíkɨ̀ nè sé à lá sə̀-í wà?",
        "traduction_exemple": (
            "Prends ce bic, est-ce que cela peut t'aider ?"
        ),
        "statut": "Entrée lexicale documentée",
        "validation_locuteur": "À effectuer",
        "source_url": (
            "https://morkegbooks.com/Services/World/Languages/"
            "SaraBagirmi/SoundDictionary/Ngambay/"
        ),
    },
    "explain": {
        "forme": "ɔ̀r̄ mḛ̀ [tàr]",
        "sens_francais": "Expliquer ; expliquer le sens d'un mot",
        "note": (
            "Construction verbale : ne pas utiliser automatiquement "
            "comme traduction d'un bouton sans adaptation."
        ),
        "statut": "Expression documentée",
        "validation_locuteur": "À effectuer",
        "source_url": (
            "https://morkegbooks.com/Services/World/Languages/"
            "SaraBagirmi/SoundDictionary/Ngambay/"
        ),
    },
})
# FIN MANASSE_NGAMBAY_ENTREES_COMPLEMENTAIRES_2026_10



# MANASSE_LEXIQUE_LIRE_ECRIRE_CREER_2026_10
# Sources : dictionnaires Ngambay et Sar de Morkeg Books.
# Les entrées restent à faire valider par des locuteurs.

LEXIQUE_LOCAL_VERIFIE["ngambay"]["entrees"].update({
    "read": {
        "forme": "túrā",
        "sens_francais": "Lire",
        "note": "Le dictionnaire donne aussi le sens « compter ».",
        "statut": "Entrée lexicale documentée",
        "validation_locuteur": "À effectuer",
        "source_url": (
            "https://morkegbooks.com/Services/World/Languages/"
            "SaraBagirmi/SoundDictionary/Ngambay/"
        ),
    },
    "write": {
        "forme": "ndàng",
        "sens_francais": "Écrire",
        "exemple": "ndàng mbēdē",
        "traduction_exemple": "Écrire une lettre",
        "statut": "Entrée lexicale documentée",
        "validation_locuteur": "À effectuer",
        "source_url": (
            "https://morkegbooks.com/Services/World/Languages/"
            "SaraBagirmi/SoundDictionary/Ngambay/"
        ),
    },
})

LEXIQUE_LOCAL_VERIFIE["sar"]["entrees"].update({
    "write": {
        "forme": "ndàng",
        "sens_francais": "Écrire",
        "exemple": "ndàng létɨ̀r",
        "traduction_exemple": "Écrire une lettre",
        "statut": "Entrée lexicale documentée",
        "validation_locuteur": "À effectuer",
        "source_url": (
            "https://morkegbooks.com/Services/World/Languages/"
            "SaraBagirmi/SoundDictionary/Sar/"
        ),
    },
    "create": {
        "forme": "ùbɨ̀",
        "sens_francais": "Créer",
        "note": (
            "Le dictionnaire documente cette forme dans le contexte "
            "de Dieu créant le ciel et la terre. Ne pas généraliser "
            "à tous les usages sans vérification."
        ),
        "statut": "Sens documenté dans un contexte précis",
        "validation_locuteur": "À effectuer",
        "source_url": (
            "https://morkegbooks.com/Services/World/Languages/"
            "SaraBagirmi/SoundDictionary/Sar/"
        ),
    },
})
# FIN MANASSE_LEXIQUE_LIRE_ECRIRE_CREER_2026_10



# MANASSE_RECHERCHE_SAR_LIRE_NGAMBAY_CREER_2026_10
# Sources : Sara Languages Lexicon et dictionnaire Ngambay de Morkeg Books.
# Validation par des locuteurs encore recommandée.

LEXIQUE_LOCAL_VERIFIE["sar"]["entrees"]["read"] = {
    "forme": "ndóō",
    "variante_transcription": (
        "ndóö dans le Sara Languages Lexicon comparatif"
    ),
    "sens_francais": "Étudier, apprendre, lire",
    "note": (
        "Le lexique présente ces trois sens dans une même entrée. "
        "Le sens précis dépend du contexte."
    ),
    "statut": "Entrée lexicale documentée",
    "validation_locuteur": "À effectuer",
    "source_url": (
        "https://morkegbooks.com/Services/World/Languages/"
        "SaraBagirmi/pdfs/SaraLanguagesLexicon.pdf"
    ),
}

LEXIQUE_LOCAL_VERIFIE["ngambay"]["entrees"].update({
    "make": {
        "forme": "ɗā",
        "sens_francais": "Faire",
        "note": (
            "Verbe général. Ne pas le considérer automatiquement "
            "comme l'équivalent de « créer »."
        ),
        "statut": "Sens général documenté",
        "validation_locuteur": "À effectuer",
        "source_url": (
            "https://morkegbooks.com/Services/World/Languages/"
            "SaraBagirmi/SoundDictionary/Ngambay/"
        ),
    },
    "build": {
        "forme": "ùndā",
        "sens_francais": "Construire",
        "note": (
            "Le dictionnaire indique le sens « construire ». "
            "Ce sens ne garantit pas une équivalence avec "
            "« créer » du contenu numérique."
        ),
        "statut": "Sens lexical documenté",
        "validation_locuteur": "À effectuer",
        "source_url": (
            "https://morkegbooks.com/Services/World/Languages/"
            "SaraBagirmi/SoundDictionary/Ngambay/"
        ),
    },
})

RECHERCHE_EN_COURS = globals().get("RECHERCHE_EN_COURS", {})
RECHERCHE_EN_COURS["ngambay"] = {
    "create": {
        "sens_recherche": "Créer, produire ou inventer quelque chose",
        "forme_confirmee": None,
        "statut": (
            "Équivalent général non confirmé dans les sources consultées."
        ),
        "candidats_voisins": [
            {"forme": "ɗā", "sens_documente": "faire"},
            {"forme": "ùndā", "sens_documente": "construire"},
        ],
        "consigne": (
            "Ne pas employer ces candidats comme traduction définitive "
            "de « créer » sans vérification contextuelle."
        ),
    },
}
# FIN MANASSE_RECHERCHE_SAR_LIRE_NGAMBAY_CREER_2026_10



# MANASSE_PRECISION_SOURCES_SAR_2026_10
# Source : Dictionnaire Sar, Morkeg Books, 2016.
# Exemples documentés dans le contexte de la création divine.

LEXIQUE_LOCAL_VERIFIE["sar"]["entrees"]["create"].update({
    "exemple": (
        "Tàgà-dɔ̀ ní Nɨ́ɓā ùbɨ̀ dɔ̀-nàng ō dɔ̀-ᶉā̰ ō."
    ),
    "traduction_exemple": (
        "Au commencement Dieu a créé la terre et le ciel."
    ),
    "note": (
        "Le dictionnaire atteste ùbɨ̀ dans le contexte de la "
        "création par Dieu. Ne pas généraliser automatiquement "
        "à la création de contenus numériques."
    ),
    "validation_locuteur": "À effectuer",
})

LEXIQUE_LOCAL_VERIFIE["sar"]["entrees"]["create_verbal_noun"] = {
    "forme": "kùbɨ̀",
    "sens_francais": "Nom verbal de créer, dans le contexte documenté",
    "exemple": "Jḭ̀ màlàng ì yá̰ kùbɨ̀ Nɨ́ɓā gɨ̄.",
    "traduction_exemple": (
        "Nous sommes tous des choses créées par Dieu."
    ),
    "statut": "Documenté dans le dictionnaire Sar",
    "validation_locuteur": "À effectuer",
    "source_url": (
        "https://morkegbooks.com/Services/World/Languages/"
        "SaraBagirmi/SoundDictionary/Sar/"
    ),
}
# FIN MANASSE_PRECISION_SOURCES_SAR_2026_10



# MANASSE_CREATE_NGAMBAY_EXPRESSION_CONTEXTUELLE_2026_10
# Source : Petit Dictionnaire de la Langue Ngambay, Morkeg Books.
# La fabrication de briques est un sens contextuel, pas un équivalent
# général de « créer » dans une application.

LEXIQUE_LOCAL_VERIFIE["ngambay"]["entrees"]["fabricate_bricks"] = {
    "forme": "ɔ̀r̄ bɔ̀rɔ̀",
    "sens_francais": "Fabriquer des briques",
    "statut": "Expression documentée dans un contexte précis",
    "validation_locuteur": "À effectuer",
    "source_url": (
        "https://morkegbooks.com/Services/World/Languages/"
        "SaraBagirmi/SoundDictionary/Ngambay/"
    ),
}

RECHERCHE_EN_COURS.setdefault("ngambay", {}).setdefault(
    "create", {}
)["forme_confirmee"] = None

RECHERCHE_EN_COURS["ngambay"]["create"]["statut"] = (
    "Aucune forme générale de « créer » confirmée pour l'instant."
)
# FIN MANASSE_CREATE_NGAMBAY_EXPRESSION_CONTEXTUELLE_2026_10



# MANASSE_NGAMBAY_POLYSEMIE_LA_2026_10
# Source : dictionnaire Ngambay de Morkeg Books.
# Même forme attestée dans deux contextes différents.

entrees_ngambay = LEXIQUE_LOCAL_VERIFIE["ngambay"]["entrees"]

entrees_ngambay["help"]["note"] = (
    "Le dictionnaire atteste aussi lá dans le sens de construire "
    "un hangar. Le contexte est indispensable pour distinguer les sens."
)

entrees_ngambay["build_hangar"] = {
    "forme": "lá",
    "sens_francais": "Construire un hangar",
    "statut": "Sens contextuel documenté",
    "validation_locuteur": "À effectuer",
    "source_url": (
        "https://morkegbooks.com/Services/World/Languages/"
        "SaraBagirmi/SoundDictionary/Ngambay/"
    ),
}

recherche_create = RECHERCHE_EN_COURS["ngambay"]["create"]
candidats = recherche_create.setdefault("candidats_voisins", [])

if not any(
    candidat.get("forme") == "lá"
    and candidat.get("sens_documente") == "construire un hangar"
    for candidat in candidats
):
    candidats.append({
        "forme": "lá",
        "sens_documente": "construire un hangar",
        "limite": "Sens contextuel, pas une traduction générale de créer",
    })

recherche_create["forme_confirmee"] = None
# FIN MANASSE_NGAMBAY_POLYSEMIE_LA_2026_10



# MANASSE_NGAMBAY_ECOUTER_2026_10
# Source : dictionnaire Ngambay de Morkeg Books,
# entrée consultable : Ngmb535.htm.

LEXIQUE_LOCAL_VERIFIE["ngambay"]["entrees"].update({
    "hear_listen": {
        "forme": "òō",
        "sens_francais": "Entendre ; écouter",
        "exemple": "Ngōn lé òō ndū bɔ̀b-é jē.",
        "traduction_exemple": (
            "L'enfant entendit la voix de ses parents."
        ),
        "autres_sens_documentes": [
            "voir",
            "savoir",
            "considérer",
        ],
        "statut": "Entrée lexicale documentée",
        "validation_locuteur": "À effectuer",
        "source_url": (
            "https://morkegbooks.com/Services/World/Languages/"
            "SaraBagirmi/SoundDictionary/Ngambay/Ngmb535.htm"
        ),
    },
})
# FIN MANASSE_NGAMBAY_ECOUTER_2026_10

def obtenir_entree(langue, cle):
    """Retourne une entrée documentée, ou None si elle n'existe pas."""
    table = LEXIQUE_LOCAL_VERIFIE.get(langue, {})
    return table.get("entrees", {}).get(cle)


def afficher_entrees(langue):
    """Affiche les expressions disponibles pour une langue."""
    table = LEXIQUE_LOCAL_VERIFIE.get(langue)
    if table is None:
        print(f"Langue inconnue : {langue}")
        return

    print(f"\n=== LEXIQUE : {table['nom']} ===")
    entrees = table.get("entrees", {})

    if not entrees:
        print("Aucune traduction d'interface validée pour le moment.")
        return

    for cle, entree in entrees.items():
        print(f"{cle} : {entree['forme']}")
        print(f"  Sens : {entree['sens_francais']}")
        print(f"  Statut : {entree['statut']}")


if __name__ == "__main__":
    afficher_entrees("ngambay")
    afficher_entrees("sar")



# MANASSEIA_CORRECTIONS_LEXIQUE_VERIFIEES_20261010
# Ajouts et précisions appuyés par les dictionnaires Morkeg Books.
# Les entrées non confirmées restent explicitement à vérifier.

_ng = LEXIQUE_LOCAL_VERIFIE["ngambay"]["entrees"]
_sa = LEXIQUE_LOCAL_VERIFIE["sar"]["entrees"]

# NGAMBAY : expliquer
_ng["explain"].update({
    "exemple": "M-ā kɔ̀r̄ mḛ̀-é dɨ̀ nāsɨ̄rā kàrī ō.",
    "traduction_exemple": "Je vais t'expliquer en français."
})

# NGAMBAY : lire et compter
_ng["read"]["sens_francais"] = "Lire ; compter"
_ng["read"]["note"] = (
    "Le dictionnaire documente túrā pour « lire » et « compter ». "
    "Un exemple complet illustrant précisément le sens « lire » "
    "reste à rechercher."
)

# NGAMBAY : écrire, avec une phrase complète du dictionnaire
_ng["write"].update({
    "exemple": (
        "ɗèē ndàng mbēdē nè lé ā-m̄ m-úlā-né "
        "m-ār ngōn-ḿ."
    ),
    "traduction_exemple": (
        "Viens écrire une lettre pour moi afin que je puisse "
        "l'envoyer à mon enfant."
    )
})

# NGAMBAY : construire
_ng["build"].update({
    "exemple": "Kə́y gɨ́ ngō-kó̰-í ùndā lé bòý yā̰ wà?",
    "traduction_exemple": (
        "La maison que ton frère a construite, est-elle grande ?"
    )
})

# NGAMBAY : entendre / écouter
_ng["hear_listen"]["traduction_exemple"] = (
    "L'enfant entendit la voix de ses parents."
)

# NGAMBAY : aider
_ng["help"]["note"] = (
    "Le dictionnaire atteste lá avec le sens « aider » et, "
    "dans un emploi distinct, « construire [un hangar] » "
    "(objet indiqué : ndíl). Il documente aussi ɗā sə̀ [də̀w̄] "
    "pour « aider quelqu'un ». Distinguer les emplois selon le contexte."
)

# NGAMBAY : construire un hangar
_ng["build_hangar"]["note"] = (
    "Le dictionnaire documente lá au sens de « construire "
    "[un hangar] » et précise l'objet ndíl. Ne pas inventer "
    "une phrase complète sans vérifier cet emploi avec la source "
    "ou un locuteur compétent."
)

# NGAMBAY : fabriquer des briques
_ng["fabricate_bricks"]["note"] = (
    "L'expression ɔ̀r̄ bɔ̀rɔ̀ est documentée au sens de "
    "« fabriquer des briques ». Exemple de phrase complète "
    "non encore vérifié."
)

# NGAMBAY : faire
_ng["make"]["note"] = (
    "Le sens général « faire » est à distinguer de « créer ». "
    "Exemple complet et traduction à vérifier avant intégration."
)

# SAR : comprendre le sens
_sa["understand"].update({
    "exemple": "à̰-á̰, m̄-gèᶉ̄ kùm àĺ ɓáy.",
    "traduction_exemple": (
        "Non, je ne comprends pas encore son sens."
    )
})

# SAR : écrire une lettre
_sa["write"].update({
    "exemple": (
        "ī-rèē ī-ndàng létɨ̀r ādɨ̄-m̄ ādɨ̄ "
        "m-ɨ́lá-ň m-ādɨ̄ ngōn-ḿ."
    ),
    "traduction_exemple": (
        "Viens écrire une lettre pour moi afin que je puisse "
        "l'envoyer à mon enfant."
    )
})

# SAR : distinguer le sens « lire » des sens documentés de ndóō.
_note_read_sar = (
    "Le dictionnaire sonore Sar consulté atteste ndóō avec les "
    "sens « enseigner », « apprendre » et « étudier ». "
    "Le sens « lire » de cette entrée comparative doit être "
    "vérifié séparément avant de l'utiliser dans une phrase."
)
_note_existante = _sa["read"].get("note", "")
if _note_read_sar not in _note_existante:
    _sa["read"]["note"] = (
        (_note_existante + " " + _note_read_sar).strip()
    )

# SAR : créer
_note_create = (
    "Le dictionnaire atteste ùbɨ̀ pour « créer » dans le contexte "
    "de la création divine, ainsi que pour « jurer ». "
    "Ne pas généraliser automatiquement ce verbe à la création "
    "de contenu numérique sans validation linguistique."
)
_note_existante = _sa["create"].get("note", "")
if _note_create not in _note_existante:
    _sa["create"]["note"] = (
        (_note_existante + " " + _note_create).strip()
    )
