from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    is_on = True
    print(logo)
    while is_on:
        options = input(f"\twhat do you want ? {menu.get_items()}: ")
        if options == "off":
            print("\nGood Bye !")
            is_on = False
        elif options == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(options)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)


main()
