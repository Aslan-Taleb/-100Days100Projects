
import random
from library import *


def main():
    myColors = color_generate("image.jpg")
    colormode(255)

    screen = Screen()
    screen.bgcolor("white")
    screen.setup(width=600, height=600)

    timmy = Turtle()
    timmy.hideturtle()
    timmy.penup()
    timmy.setx(-250)
    timmy.sety(-250)
    timmy.speed("fastest")

    step = 50

    for _ in range(10):
        for _ in range(10):
            pos_x, pos_y = timmy.position()
            timmy.pendown()
            timmy.dot(20, random.choice(myColors))
            timmy.penup()
            timmy.goto(pos_x+step, pos_y)
        timmy.setx(-250)
        timmy.sety(pos_y+50)

    screen.exitonclick()


main()
