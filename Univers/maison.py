def actualiser_points_maison(maisons, nom_maison, points) :
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }
    if nom_maison in  maisons :
        maisons[nom_maison] += points
        print(f"{nom_maison} a recu {points} points. Nouveaux Total :{points} ")
    else :
        print(f"{nom_maison} introuvable")

