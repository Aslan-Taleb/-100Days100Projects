from library import * 
from logo import *
from replit import clear


def main():
    end_game = False
    print(logo)
    print("Welcome to the Number Guessing Game!")
    while not end_game:
        print("I'm thinking of a number between 1 and 100.")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        want_continue = play(difficulty)
        if want_continue == 'n':
            end_game = True
            print("\n")
        else:
            clear()
        
    print("Thanks for playing!")
       
    
main()