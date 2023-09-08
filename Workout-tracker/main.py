from library import *
from art import *


def main():
    # Afficher le logo
    print(logo)
    # Demander les informations utilisateur si elles n'ont pas été fournies précédemment
    # Menu principal
    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Enregistrer un nouvel exercice")
        print("2. Quitter")

        choice = input("Entrez le numéro de votre choix : ")

        if choice == "1":
            result = get_exercice()
            for exercise in result["exercises"]:
                add_row(exercise["name"].title(), exercise["duration_min"], exercise["nf_calories"])
            print("\nL'exercice a été enregistré avec succès !")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("\nChoix invalide. Veuillez entrer un choix valide.")


main()
