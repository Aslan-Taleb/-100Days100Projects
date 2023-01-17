from art import * 
from library import * 


def main():
    stop = False
    stop_programm = ""
    print(logo)
    while not stop:
        name = input("What is your name ? : ")
        price = int(input("What's your bid ? : $"))
        add_bidder(name,price)
        stop_programm = input("Are there any other bidders? Types 'yes' or 'no'.\n")
        if stop_programm == 'no':
            stop = True
        else:
            clear()
    who_won()
    
    
main()