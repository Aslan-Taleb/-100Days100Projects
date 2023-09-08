from library import *
from art import *


def main():
    print(logo)
    while True:
        choice = welcome()
        if choice == "1":
            choose_movie()
        elif choice == "2":
            view_watched()
        elif choice == "3":
            print("Thanks for using the Movie Selector! (c'est Ciao)")
            exit()
        else:
            print("Invalid choice\n")


main()
