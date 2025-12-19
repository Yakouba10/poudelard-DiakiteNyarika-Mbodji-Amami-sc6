def initialiser_personnage(nom, prenom, attributs):


    personage={
        "nom": nom,
        "prenom": prenom,
        "attributs": attributs,
        "Argent": 100,
        "Inventaire": [],
        "Sortiléges": []

    }
    return personage


def afficher_personnage(joueur):
    """
    Affiche proprement toutes les informations du personnage.
    """
    print("Profil du personnage :")

    for cle, valeur in joueur.items():
        if isinstance(valeur, dict):
            print(f"{cle} :")
            for scle, sval in valeur.items():
                print(f" - {scle} : {sval}")
        elif isinstance(valeur, list):
            contenu = ", ".join(str(x) for x in valeur)
            print(f"{cle} : {contenu}")

        else:
            print(f"{cle} : {valeur}")



def modifier_argent(joueur, montant):
    """
    Ajoute (ou retire) un montant au joueur.
    montant peut être positif ou négatif.
    """
    joueur["Argent"] += montant



def ajouter_objet(joueur, cle, objet):
    """
    Ajoute un objet dans Inventaire ou Sortilèges.
    cle doit être 'Inventaire' ou 'Sortilèges'.
    objet est une chaîne.
    """
    if cle not in ["Inventaire", "Sortilèges"]:
        print("Erreur : clé invalide (doit être 'Inventaire' ou 'Sortilèges').")
        return


    (joueur[cle].append(objet))


