from library import *
from art import *
def main():
    print(logo)
    myInput = ""
    while True:
        while myInput != "espresso" and myInput != "latte" and myInput != "cappuccino" and myInput != "report":
            myInput = input("What would you like? (espresso/latte/cappuccino): ").lower()
            money(myInput)
            myInput = ""
        
main()