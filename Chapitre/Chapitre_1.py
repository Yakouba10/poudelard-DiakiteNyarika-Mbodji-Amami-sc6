def introduction():
    print ("Bonjour et bienvenue dans le jeu. L'histoire commence ... ")

def creer_personnage():
    personnage={}
    personnage["nom_personnage"] = input("Entrez le nom du personnage : ")
    personnage["prenom_personnage"] = input("Entrez le prénom du personnage : ")
    personnage["note_courage"] = input("Entrez une valeur de 1 à 10 pour évaluer votre courage : ")
    personnage["note_intelligence"] = input("Entrez une valeur de 1 à 10 pour évaluer votre intelligence : ")
    personnage["note_loyaute"] = input("Entrez une valeur de 1 à 10 pour évaluer votre loyauté : ")
    personnage["note_ambition"]= input("Entrez une valeur de 1 à 10 pour évaluer votre ambition : ")

    return(personnage)

def initialiser_personnage(personnage):
    print( "PROFIL DU PERSONNAGE \n\n"
           "NOM : ", personnage["nom_personnage"] + "\n" +
           "PRENOM : ", personnage["prenom_personnage"] + "\n\n " +
           "QUALITES : \n"
           "    COURAGE : ", personnage["note_courage"] + "\n" +
           "    INTELLIGENCE : ", personnage["note_intelligence"] + "\n" +
           "    LOYAUTE : ", personnage["note_loyaute"] + "\n"
           "    AMBITION : ", personnage["note_ambition"])
