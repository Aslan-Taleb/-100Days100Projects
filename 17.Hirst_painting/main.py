
import random
from library import *


def main():
    timmy = Turtle()
    colormode(255)
    timmy.pensize(20)
    myColors = color_generate("image.jpg")
    go = 50
    timmy.penup()
    timmy.setx(-100)
    timmy.sety(-100)
    pos_y = -350

    while True:
        for _ in range(10):
            pos_x, _ = timmy.position()
            timmy.pendown()
            timmy.dot(random.choice(myColors))
            timmy.penup()
            timmy.goto(pos_x+go, pos_y)
        timmy.setx(-100)
        pos_y += 10

    myScreen()


main()
