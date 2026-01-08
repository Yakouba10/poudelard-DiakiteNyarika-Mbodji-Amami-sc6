def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    liste_joueur = list(equipe_data[maison]["joueurs"])

    equipe = {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "joueurs": liste_joueur
    }

    if est_joueur and joueur is not None:
        liste_joueur2 = []
        joueur_principal = f"{joueur} (Attrapeur)"
        liste_joueur2.append(joueur_principal)

        for j in equipe["joueurs"]:
            nom_joueur = j.split(" (")[0]
            if nom_joueur != joueur:
                liste_joueur2.append(j)

        equipe["joueurs"] = liste_joueur2

    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):

    proba_but = random.randint(1, 10)
    if proba_but >= 6:

        if joueur_est_joueur:
            buteur = equipe_attaque["joueurs"][0]
        else:
            buteur = random.choice(equipe_attaque["joueurs"])

        equipe_attaque["score"] = equipe_attaque["score"] + 10
        equipe_attaque["a_marque"] = equipe_attaque["a_marque"] + 1

        print(buteur, "marque un but pour", equipe_attaque["nom"], "! (+10 points)")


    else:
        equipe_defense["a_stoppe"] = equipe_defense["a_stoppe"] + 1
        print(equipe_defense["nom"], "bloque l'attaque !")
