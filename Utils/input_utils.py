def demander_choix(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        choix = input("Votre choix : ")
        if choix.isdigit():
            choix = int(choix)
            if 1 <= choix <= len(options):
                return options[choix - 1]
        print("Choix invalide, recommence.")


def load_fichier(chemin):
    import json
    with open(chemin, "r", encoding="utf-8") as fichier:
        return json.load(fichier)
