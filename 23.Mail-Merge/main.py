from art import *
from library import create_letter


def main():
    print(logo_start)
    print("Welcome to the 'Mail Rejection 3000'")
    choice = input("Do you want to make people Sad ? yes / no\nchoice : ")
    if choice == "yes":
        print("Starting writing...")
        number_letter = create_letter()
        print("Go Check your Files Output/ReadyToSend\n")
        print(f"congratulations you made {number_letter} people sad ! ")
    else:
        print("Good,well dont use this program,Good bye!")


main()
