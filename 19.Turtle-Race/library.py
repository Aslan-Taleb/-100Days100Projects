from turtle import *
from random import *

colors = ["red", "orange", "green", "yellow", "blue", "purple"]


def turtle_hiring():
    turtle_list = []
    for i in range(5):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        turtle_list.append(new_turtle)
    return turtle_list


def position_turtle(turtle_list):
    up_down = -120
    for turtle in turtle_list:
        turtle.goto(x=-240, y=up_down)
        up_down += 35
    return turtle_list


def race(turtle_list):
    for turtle in turtle_list:
        if turtle.xcor() > 222:
            winner = turtle
            return winner
        speed = randint(1, 10)
        turtle.forward(speed)


def winner_bet(winner, theBet, screen):
    screen.clear()
    screen.bgpic("winner_loser.png")
    winner.goto(0, 0)
    if winner.pencolor() == theBet:
        winner.write(f"You've won! The {winner.pencolor()} turtle is the winner!",
                     False, align="center", font=('italic', 15, 'italic'))
    else:
        print()
        winner.write(f"You've lost! The {winner.pencolor()} turtle is the winner!", font=(
            'italic', 15, 'italic'), align="center")
