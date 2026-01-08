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
