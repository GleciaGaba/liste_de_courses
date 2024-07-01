import sys
import json




MENU = """Choississez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la list 
4: Vider la list
5: Quitter
Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]


with open("liste_correction.json", "r") as fichier:
        LISTE = json.load(fichier)


while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")


    if user_choice == "1":
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")




    elif user_choice == "2":  # Retirer un élément
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")




    elif user_choice == "3":  # Afficher la liste
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.")


    elif user_choice == "4":  # Vider la liste
        LISTE.clear()
        print("La liste a été vidée de son contenu.")

    elif user_choice == "5":  # Sauvegarder et quitter
        with open(LISTE_PATH, "w") as f:
            json.dump(LISTE, f, indent=4)
        print("À bientôt !")
        sys.exit()

    print("-" * 50)