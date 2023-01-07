from draws import *

print(homer)

print("Welcome to Donut Island.")
print("Your mission is to find the sugar donut with sugar.")

choice = ""
test = False
while not (test):
    choice = input(
        'You are at a cross road.Where do you want to go ? Type "left" or "right"\n')
    choice = choice.lower()
    if choice == "left" or choice == "right":
        test = True
    else:
        print(doh)
        print("\nRetry ...(focus it's not complicated)")

if choice == "right":
    print(gameover)
    print("\nGame Over !!")
    wait()

else:
    test = False
    while not (test):
        print(island)
        choice = input(
            'You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat.Type "swim" to swim across.\n')
        choice = choice.lower()
        if choice == "swim" or choice == "wait":
            test = True
        else:
            print(doh)
            print("\nRetry ...(focus it's not complicated")
    if choice == "swim":
        print(gameover)
        print("\nGame Over !!")
        wait()
        
    else:
        test = False
        while not (test):
            print(open)
            choice = input(
                'You arrive at the island unharmed. There is a house with 3 doors. One "red",one "yellow" and one "blue".Which colour do you choose?\n')
            choice = choice.lower()
            if choice == "red" or choice == "blue" or choice == "yellow":
                test = True

            else:
                print(doh)
                print("\nRetry ...(focus it's not complicated")
    if choice == "red":
        print(cartman)
        print("Cartman just ate the Donut..Game Over ! ")
        wait()
    elif choice == "blue":
        print(hitman)
        print("Hitman just put a bullet in your head..Game Over")
        wait()
    elif choice == "Yellow":
        print(victory)
        print("VICTORY !!!")
        wait()

#Made By AslaN