def introduction():
    print ("Bonjour et bienvenue dans le jeu. L'histoire commence ... ")

def creer_personnage():
    attributs={}
    nom = input("Entrez le nom du personnage : ")
    prenom = input("Entrez le prénom du personnage : ")
    attributs["note_courage"] = input("Entrez une valeur de 1 à 10 pour évaluer votre courage : ")
    attributs["note_intelligence"] = input("Entrez une valeur de 1 à 10 pour évaluer votre intelligence : ")
    attributs["note_loyaute"] = input("Entrez une valeur de 1 à 10 pour évaluer votre loyauté : ")
    attributs["note_ambition"]= input("Entrez une valeur de 1 à 10 pour évaluer votre ambition : ")

    print( "PROFIL DU PERSONNAGE \n\n"
           "NOM : ", nom + "\n" +
           "PRENOM : ", prenom + "\n\n " +
           "ATTRIBUTS : \n"
           "    COURAGE : ", attributs["note_courage"] + "\n" +
           "    INTELLIGENCE : ", attributs["note_intelligence"] + "\n" +
           "    LOYAUTE : ", attributs["note_loyaute"] + "\n"
           "    AMBITION : ", attributs["note_ambition"])

    return(nom, prenom, attributs)


def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard…"
          "\n\n« Cher élève nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »"
            "\n\nSouhaitez-vous accepter cette invitation et partir pour Poudlard ?"+"\n1. Oui, bien sûr !\n2. Non, je préfère rester avec l’oncle Vernon…")

    reponse = input()
    if reponse != "1" and reponse != "2":
        exit('Mauvaise saisie. Fin du jeu')

    if reponse == "2":
        print("\n\n Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: « EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » "
              "Le monde magique ne saura jamais que vous existiez... \nFin du jeu !")
        exit(0)

def rencontrer_hagrid():
    print(" Hagrid : Salut. Je suis venu t'aider à faire tes achats sur le chemin de Traverse.\n\n"
                                                            "Voulez vous suivre Hagrid ?\n\n1. Oui\n\n2. Non")
    reponse=input()
    if reponse != "1" and reponse != "2": exit()
    if reponse == "2": print("\nFais moi confiance tu dois me suivre, tu ne le regrettera pas !")


