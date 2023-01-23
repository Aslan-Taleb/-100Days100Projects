from Menu import *


def espresso():
    '''Return if there is enought ingredients to do the espresso Boolean'''
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
    '''Return if there is enought ingredients to do the latte Boolean'''
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
    '''Return if there is enought ingredients to do the cappuccino Boolean'''
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
    '''return If there is enought ingredients Boolean'''
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
    
    
def money(myInput):
    '''Take coins and return the refund a make the drink '''
    coins = 0
    refund = 0
    if myInput != "report" and myInput != "off":
        price = MENU[myInput]['cost']
        print("Please insert coins.")
        print("we gonna use 'Algerian dinar'(it's my machine i do what i want)")
        print(f"Price : {MENU[myInput]['cost']} DA.\n")
        coins+=int(input("how many piece of 200 DA?: ")) * 200
        coins+=int(input("how many piece of 100 DA?: ")) * 100
        coins+=int(input("how many piece of 50 DA?: ")) * 50
        coins+=int(input("how many piece of 20 DA?: ")) * 20
        if coins >= price:
            if check_ingredients(myInput):
                refund = coins- price
                if refund > 0: 
                    print(f"Here is {refund}DA in change.")
                print(f"Here is your {myInput} ☕️. Enjoy!")
                resources["money"] += price
                return True  
            else:
                print(f"Here is your {coins} ☕️. Enjoy!")
                
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        check_ingredients(myInput)
        return 0
            
            
            
        
        
        
        
        
        
    
    
