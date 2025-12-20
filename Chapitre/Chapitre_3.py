import json
import random

def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    print("Tu commences tes cours de magie à Poudlard...")

    fichier = open(chemin_fichier, "r", encoding="utf-8")
    sorts = json.load(fichier)
    fichier.close()

    joueur["Sortilèges"] = []

    nb_offensif = 0
    nb_defensif = 0
    nb_utilitaire = 0

    while len(joueur["Sortilèges"]) < 5:
        sort = random.choice(sorts)

        if sort in joueur["Sortilèges"]:
            continue

        if sort["type"] == "Offensif" and nb_offensif < 1:
            nb_offensif = nb_offensif + 1

        elif sort["type"] == "Défensif" and nb_defensif < 1:
            nb_defensif = nb_defensif + 1

        elif sort["type"] == "Utilitaire" and nb_utilitaire < 3:
            nb_utilitaire = nb_utilitaire + 1

        else:
            continue

        joueur["Sortilèges"].append(sort)
        print("Tu viens d'apprendre le sortilège :", sort["nom"], "(", sort["type"], ")")
        input("Appuie sur Entrée pour continuer...")

    print("Tu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")

    for sort in joueur["Sortilèges"]:
        print("-", sort["nom"], "(", sort["type"], ") :", sort["description"])
import json
import random

def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):
    fichier = open(chemin_fichier, "r", encoding="utf-8")
    quiz = json.load(fichier)
    fichier.close()

    print("Bienvenue au quiz de magie de Poudlard !")

    score = 0
    questions_choisies = []

    while len(questions_choisies) < 4:
        question = random.choice(quiz)
        if question not in questions_choisies:
            questions_choisies.append(question)

    numero = 1
    for q in questions_choisies:
        print(numero, ".", q["question"])
        reponse = input("> ")

        if reponse.lower() == q["reponse"].lower():
            print("Bonne réponse ! +25 points pour ta maison.")
            score = score + 25
        else:
            print("Mauvaise réponse. La bonne réponse était :", q["reponse"])

        numero = numero + 1

    print("Score obtenu :", score)
    joueur["score"] = joueur["score"] + score

def lancer_chapitre_3(personnage, maisons):
    apprendre_sorts(personnage)
    quiz_magie(personnage)

    maison_joueur = personnage["maison"]
    maisons[maison_joueur] = maisons[maison_joueur] + personnage["score"]

    maison_en_tete = max(maisons, key=maisons.get)
    print("Maison actuellement en tête :", maison_en_tete)

    print("Informations du joueur :")
    print(personnage)
