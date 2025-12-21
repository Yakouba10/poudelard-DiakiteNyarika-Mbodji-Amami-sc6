def demander_texte(message):
    return input(message)

def demander_nombre(message, min_val=None, max_val=None):
    while True:
        try:
            valeur = int(demander_texte(message))

            if min_val is not None and valeur < min_val:
                print(f"Erreur : Choisir une valeur comprise entre 1 et 10")
                continue

            if max_val is not None and valeur > max_val:
                print(f"Erreur : Choisir une valeur comprise entre 1 et 10")
                continue

            return valeur

        except ValueError:
            print("Erreur : Choisir un nombre entier.")


def demander_choix(message, options):
    rep= False

    while not rep:
        print(message)
        compteur = 1
        for i in options:
            print(str(compteur) + "." + str(i))
            compteur = compteur + 1

        try:
            choix = int(demander_texte(" "))

            if 1 <= choix <= len(options):
                rep = True
                return choix
            else:
                print("Mauvaise saisie, veuillez recommencer.\n")

        except ValueError:
            print("Mauvaise saisie, veuillez recommencer.\n")


def load_fichier(chemin):
    import json
    with open(chemin, "r", encoding="utf-8") as fichier:
        return json.load(fichier)

