from Utils.input_utils import demander_texte, demander_nombre, demander_choix


def introduction():
    print ("Bonjour et bienvenue dans le jeu. L'histoire commence ... ")

def creer_personnage():
    attributs={}
    nom = demander_texte("Entrez le nom du personnage : ")
    prenom = demander_texte("Entrez le prénom du personnage : ")
    attributs["note_courage"] = demander_nombre("Entrez une valeur de 1 à 10 pour évaluer votre courage : ",1,10)
    attributs["note_intelligence"] =demander_nombre("Entrez une valeur de 1 à 10 pour évaluer votre intelligence : ",1,10)
    attributs["note_loyaute"] = demander_nombre("Entrez une valeur de 1 à 10 pour évaluer votre loyauté : ",1,10)
    attributs["note_ambition"]= demander_nombre("Entrez une valeur de 1 à 10 pour évaluer votre ambition : ",1,10)

    return(nom, prenom, attributs)

def recevoir_lettre():

    reponse = demander_choix("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard…"
          "\n\n« Cher élève nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »"
            "\n\nSouhaitez-vous accepter cette invitation et partir pour Poudlard ?",["\nOui, bien sûr !","\nNon, je préfère rester avec l’oncle Vernon…"])

    if reponse == "2":
        print("\n\n Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: « EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » "
              "Le monde magique ne saura jamais que vous existiez... \nFin du jeu !")
        exit(0)

def rencontrer_hagrid():

    reponse=demander_choix(" Hagrid : Salut. Je suis venu t'aider à faire tes achats sur le chemin de Traverse.\n\n"
                                                            "Voulez vous suivre Hagrid ?", ["Oui","Non"])
    if reponse == "2": print("\nFais moi confiance tu dois me suivre, tu ne le regrettera pas !")




