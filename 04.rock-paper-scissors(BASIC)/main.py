#Made by AslaN
from draws import *
import random as r
print("Welcome to the Rock Paper Scissors game.")
end = False
while(not(end)):
    test = False
    while not(test):
        choice = int(input("What do you choose? Type 0 for Rock,1 for Paper,2 for Scissors or 3 for a well.\n"))
        if choice == 0 or choice == 1 or choice == 2:
            test = True
        elif choice == 3:
            print("Bro,we dont do that here..")
        else:
            print("Focus Please it's an ancient game")
            
    thePlayer = play(choice)
    print("Computer choose:\n")
    theCPU = play(r.randint(0,2))
    end= rules(thePlayer,theCPU)

