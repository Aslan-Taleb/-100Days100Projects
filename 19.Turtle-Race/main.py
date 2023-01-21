from library import *


def main():
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.title("The Turtle Race")
    screen.bgpic("background.png")

    is_race_on = False
    theBet = ""
    winner = None
    print_colors = '\n'.join(colors)

    while theBet not in colors:
        theBet = screen.textinput(
            title="Make your bet", prompt=f"Which turtle will win the race ? \n{print_colors}\n➜Enter a color : ").lower()

    if theBet:
        is_race_on = True

    myListofTurtle = turtle_hiring()
    position_turtle(myListofTurtle)
    while is_race_on:
        winner = race(myListofTurtle)
        if winner != None:
            is_race_on = False
    winner_bet(winner, theBet, screen)

    screen.exitonclick()


main()
