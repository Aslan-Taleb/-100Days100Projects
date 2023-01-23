# the bill input
print("Welcome to the tip calculator")
bill = float(input("What was the total bill ? $"))

percentage = 0
test = False
theTip = [10, 12, 15]
# the tip input
while (test != True):
    percentage = int(
        input(f"What percentage tip would you like to give ?{theTip[0]},{theTip[1]}, or {theTip[2]} ? "))
    if (percentage == theTip[0] or percentage == theTip[1] or percentage == theTip[2]):
        test = True
    else:
        print("ERROR choose 10,12,or 15")

# the people input
people = int(input("How many people to split the bill ? "))

# calcul the tip
if people != 0:
    tip = (percentage * bill)/100
    toPay = (bill + tip) / people
    # rounding 'toPay'
    # we can use this toPay = round(toPay, 2) BUT it will not print the decimal if it's '0'
    toPay = "{:.2f}".format(toPay) #<-so we use this (it's transform it into a string..)
    print(f"Each person should pay : ${toPay}")
else:
    print("ERROR : 0 person")

# Made by AslaN
