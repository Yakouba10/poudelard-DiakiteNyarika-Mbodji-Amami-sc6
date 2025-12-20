maisons = {
"Gryffondor": 0,
"Serpentard": 0,
"Poufsouffle": 0,
"Serdaigle": 0
}
def actualiser_points_maison(maisons, nom_maison, points) :

    if nom_maison in  maisons :
        maisons[nom_maison] += points
        print(f"{nom_maison} a recu {points} points. Nouveaux Total :{points} ")
    else :
        print(f"{nom_maison} introuvable")

def afficher_maison_gagnante(maisons) :
    max_points = max(maisons.values())
    liste_gagnante = []
    for nom_maison, points in maisons.items() :
        if points == max_points :
            liste_gagnante.append(nom_maison)
    if len(liste_gagnante) == 1 :
        print(f" liste_gagnante[0] a gagné")
    else :
        print("Egalité entre ", *liste_gagnante, sep=" ,")


questions = [
    (
        "Tu vois un ami en danger. Que fais-tu ?",
        ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l'aide" , "calme et j'observe"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    ),
    (
        "Quel trait te décrit le mieux ?",
        ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    ),
    (
        "Face à un défi difficile, tu...",
        ["Fonces sans hésiter", "Cherches la meilleure stratégie",
         "Comptes sur tes amis", "Analyses le problème"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    )
]
def repartition_maison(joueur, questions) :
    scores = {
        "Gryffondor": 0,
        "Serdaigle": 0,
        "Poufsouffle": 0,
        "Serpentard": 0
    }
    scores["Gryffondor"] += joueur["courage"] * 2
    scores["Serpentard"] += joueur["ambition"] * 2
    scores["Poufsouffle"] += joueur["loyaute"] * 2
    scores["Serdaigle"] += joueur["intelligence"] * 2
    for question, choix, maisons in questions:
        print(question)
        print("1.", choix[0])
        print("2.", choix[1])
        print("3.", choix[2])
        print("4.", choix[3])

        reponse = int(input("Ton choix : "))
        maison = maisons[reponse - 1]
        scores[maison] = scores[maison] + 3
        print()
        maison_finale = max(scores, key=scores.get)

        return maison_finale



