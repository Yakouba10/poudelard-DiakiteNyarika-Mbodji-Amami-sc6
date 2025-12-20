import utils.input_utils
import univers.maison
import univers.personnage

def rencontrer_amis(joueur):
    print("\nVous montez à bord du Poudlard Express...\n")

    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?")
    choix = utils.input_utils.demander_choix(
        "Que répondez-vous ?",
        ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."]
    )

    if choix == "Bien sûr, assieds-toi !":
        joueur["Attributs"]["loyauté"] += 1
    else:
        joueur["Attributs"]["ambition"] += 1

    print("\n— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    choix = utils.input_utils.demander_choix(
        "Que répondez-vous ?",
        ["Oui, j’adore apprendre de nouvelles choses !",
         "Euh… non, je préfère les aventures aux bouquins."]
    )

    if choix.startswith("Oui"):
        joueur["Attributs"]["intelligence"] += 1
    else:
        joueur["Attributs"]["courage"] += 1

    print("\n— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    choix = utils.input_utils.demander_choix(
        "Comment réagissez-vous ?",
        ["Je lui serre la main poliment.",
         "Je l’ignore complètement.",
         "Je lui réponds avec arrogance."]
    )

    if choix.startswith("Je lui serre"):
        joueur["Attributs"]["ambition"] += 1
    elif choix.startswith("Je l’ignore"):
        joueur["Attributs"]["loyauté"] += 1
    else:
        joueur["Attributs"]["courage"] += 1

    print("\nAttributs mis à jour :", joueur["Attributs"])





