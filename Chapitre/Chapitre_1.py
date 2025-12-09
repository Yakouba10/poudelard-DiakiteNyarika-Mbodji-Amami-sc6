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

def rencontrer_hagrid(personnage):
    print(" Hagrid : Salut "+personnage["prenom_personnage"]+". Je suis venu t'aider à faire tes achats sur le chemin de Traverse.\n\n"
                                                            "Voulez vous suivre Hagrid ?\n\n1. Oui\n\n2. Non")
    reponse=input()
    if reponse != "1" and reponse != "2": exit()
    if reponse == "2": print("\nFais moi confiance tu dois me suivre, tu ne le regrettera pas !")

