from Univers.personnage import afficher_personnage
from Utils.input_utils import demander_texte, demander_nombre, demander_choix, load_fichier


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

    reponse = demander_choix("\n\nUne chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard…"
          "\n\n« Cher élève nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »"
            "\n\nSouhaitez-vous accepter cette invitation et partir pour Poudlard ?",["Oui, bien sûr !","Non, je préfère rester avec l’oncle Vernon…"])

    if reponse == "2":
        print("\n\n Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: « EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » "
              "Le monde magique ne saura jamais que vous existiez... \nFin du jeu !")
        exit(0)

def rencontrer_hagrid():

    reponse=demander_choix("\n\nHagrid : Salut. Je suis venu t'aider à faire tes achats sur le chemin de Traverse.\n\n"
                                                            "Voulez vous suivre Hagrid ?", ["Oui","Non"])
    if reponse == "2": print("\nFais moi confiance tu dois me suivre, tu ne le regrettera pas !")

def acheter_fournitures(personnage):
    fichier = load_fichier("/Users/ines/PycharmProjects/poudelard-DiakiteNyarika-Mbodji-Amami-sc6/Data/inventaire.json")
    print("Catalogue des objets disponibles :\n")
    for cle in fichier:
        nom = fichier[cle][0]
        prix = fichier[cle][1]
        print(f"{cle}. {nom} - {prix} galions")
    print("\nVous avez 100 galions.")

    print("\nObjets obligatoires restant à acheter : Baguette magique, Robe de sorcier, Manuel de potions")
    objets = [
        "Baguette magique - 35 galions",
        "Robe de sorcier - 20 galions",
        "Manuel de potions - 25 galions"
    ]

    while len(objets) > 0:
        rep = demander_choix(
            "\nEntrez le numéro de l'objet à acheter :\n",
            objets)

        objet_achete = objets[rep - 1]
        print(f"Vous avez acheté : {objet_achete}")
        objets.pop(rep - 1)

    print("\nTous les objets obligatoires ont été achetés !")
    print("\nIl est temps de choisir votre animal de compagnie pour Poudlard !\n\nVous avez 20 galions."
          "\n\nVoici les animaux disponibles : \n\n• Chouette - 20 galions \n• Chat - 15 galions \n• Rat - 10 galions\n• Crapaud - 5 galions")
    rep = demander_choix("\nQuel animal voulez-vous ?",
                         ["Chouette - 20 galions", "Chat - 15 galions", "Rat - 10 galions", "Crapaud - 5 galions"])
    if rep == 1: print("\nVous avez choisi : Chouette (-20 galions)")
    if rep == 2: print("\nVous avez choisi : Chat - 15 galions")
    if rep == 3: print("\nVous avez choisi : Rat - 10 galions")
    if rep == 4: print("\nVous avez choisi : Crapaud - 5 galions")

    print("\nTous les objets obligatoires ont été achetés avec succès ! Voici votre inventaire final :")

    #probleme avec la synchronisation des personnages
    #afficher_personnage(personnage)

def chapitre1():
    introduction()
    perso=creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid()
    acheter_fournitures(perso)
    return(perso)

    print("\nFin du Chapitre 1 ! Votre aventure commence à Poudlard..")




