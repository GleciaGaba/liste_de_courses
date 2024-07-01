import json
import sys

liste = []
while True:
    print("---------------------------------------------------------------------------------------------")
    print("Choisissez parmi les 5 options suivantes: ")
    print("1: Ajouter un élément à la liste de courses")
    print("2: Retirer un élément de la liste de courses")
    print("3: Afficher les éléments de la liste de courses")
    print("4: Vider la liste de courses")
    print("5: Quitter le programme")

    choix = input()
    print(f"Votre choix : {choix}")



    if choix == "1":
        element_ajouter = input("Entrez le nom d'un élément à ajouter à la liste de course : ").title()
        print(f"L'élément {element_ajouter} a bien été ajouté à la liste.")
        liste.append(element_ajouter)
        print(f"Voici le contenu de votre liste: {liste}")
        with open("liste.json", "w") as fichier:
            json.dump(liste, fichier)
        with open("liste.json", "r") as fichier:
            result = json.load(fichier)
        result.append(liste)



    elif choix == "2":
        element_retirer = input("Entrez le nom d'un élément à retirer à la liste de course : ").title()
        # liste = [x for x in liste if x != element_retirer]

        with open("liste.json", "r") as fichier:
            result = json.load(fichier)
        liste = [x for x in result if x != element_retirer]
        with open("liste.json", "w") as fichier:
            json.dump(liste, fichier, indent=4)



    elif choix == "3":

        with open("liste.json", "r") as fichier:
            result = json.load(fichier)
        for i, element in enumerate(result):
            print(f"Voici le contenu de votre liste: {i, element}")



    elif choix == "4":
        with open("liste.json", "r") as fichier:
            clean_list = json.load(fichier)
        clean_list.clear()
        with open("liste.json", "w") as fichier:
            json.dump(clean_list, fichier)


    elif choix == "5":
        sys.exit()


    else:
        print("Veuillez écrire les chiffres entre 1 et 5.")
