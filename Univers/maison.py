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
