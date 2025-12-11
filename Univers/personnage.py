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
        # Cas 1 : dictionnaire (ex : attributs)
        if isinstance(valeur, dict):
            print(f"{cle} :")
            for scle, sval in valeur.items():
                print(f" - {scle} : {sval}")

        # Cas 2 : liste (inventaire, sortilèges)
        elif isinstance(valeur, list):
            # jointure en chaîne si la liste n'est pas vide
            contenu = ", ".join(str(x) for x in valeur)
            print(f"{cle} : {contenu}")

        # Cas 3 : valeur simple
        else:
            print(f"{cle} : {valeur}")

