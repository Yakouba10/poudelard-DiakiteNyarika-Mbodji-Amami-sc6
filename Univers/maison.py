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





