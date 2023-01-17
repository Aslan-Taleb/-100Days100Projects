from Menu import *


def espresso():
    ingr1 = False
    ingr2 = False
    if resources["water"] >= MENU['espresso']['ingredients']['water']:
        resources["water"] = resources["water"] - \
            MENU['espresso']['ingredients']['water']
        ingr1 = True
    else:
        print("Sorry there is not enough water.")
        return False
    if resources["coffee"] >= MENU['espresso']['ingredients']['coffee']:
        resources["coffee"] = resources["coffee"] - \
            MENU['espresso']['ingredients']['coffee']
        ingr2 = True
    else:
        print("Sorry there is not enough coffee.")
        return False
    return ingr1 and ingr2


def latte():
    ingr1 = False
    ingr2 = False
    ingr3 = False
    if resources["water"] >= MENU['latte']['ingredients']['water']:
        resources["water"] = resources["water"] - \
            MENU['latte']['ingredients']['water']
        ingr1 = True
    else:
        print("Sorry there is not enough water.")
        return False
    if resources["coffee"] >= MENU['latte']['ingredients']['coffee']:
        resources["coffee"] = resources["coffee"] - \
            MENU['latte']['ingredients']['coffee']
        ingr2 = True
    else:
        print("Sorry there is not enough coffee.")
        return False
    if resources["milk"] >= MENU['latte']['ingredients']['milk']:
        resources["milk"] = resources["milk"] - \
            MENU['latte']['ingredients']['milk']
        ingr3 = True
    else:
        print("Sorry there is not enough milk.")
        return False
    return ingr1 and ingr2 and ingr3


def cappuccino():
    ingr1 = False
    ingr2 = False
    ingr3 = False
    if resources["water"] >= MENU['cappuccino']['ingredients']['water']:
        resources["water"] = resources["water"] - \
            MENU['cappuccino']['ingredients']['water']
        ingr1 = True
    else:
        print("Sorry there is not enough water.")
        return False
    if resources["coffee"] >= MENU['cappuccino']['ingredients']['coffee']:
        resources["coffee"] = resources["coffee"] - \
            MENU['cappuccino']['ingredients']['coffee']
        ingr2 = True
    else:
        print("Sorry there is not enough coffee.")
        return False
    if resources["milk"] >= MENU['cappuccino']['ingredients']['milk']:
        resources["milk"] = resources["milk"] - \
            MENU['cappuccino']['ingredients']['milk']
        ingr3 = True
    else:
        print("Sorry there is not enough milk.")
        return False
    return ingr1 and ingr2 and ingr3


def check_ingredients(myInput):

    if myInput == "report":
        print(f"the current resource values : \n{resources}")
        return 0
    elif myInput == "off":
        print("machine shutdown...")
        exit()
    elif myInput == "espresso":
        return espresso()
    elif myInput == "latte":
        return latte()
    elif myInput == "cappuccino":
        return cappuccino()
