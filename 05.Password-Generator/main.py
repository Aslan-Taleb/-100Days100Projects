#Made by AslaN
#Password Generator Project
from function import *




def main():
    test = False
    print(intro)
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password? ")) 
    nr_symbols = int(input(f"How many symbols would you like? "))
    nr_numbers = int(input(f"How many numbers would you like? "))

    while not(test):
        mode = input(f"Normal security (n) or the highest one (m)  ? ")
        if mode =="m" or mode == "n":
            test = True
        else:
            print("Focus..or i leak your password ! (just kidding..i mean you never know)")   
    if mode == "n":
        ez(nr_letters,nr_symbols,nr_numbers)
    else:
        hard(nr_letters,nr_symbols,nr_numbers)
main()
    
