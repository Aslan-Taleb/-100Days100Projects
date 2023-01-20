from turtle import *
import colorgram as c


def myScreen():
    screen = Screen()
    screen.colormode(255)
    screen.screensize(1000, 1000)
    screen.exitonclick()


def color_generate(image):
    colors = c.extract(image, 35)
    myColors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        myColors.append((r, g, b))
    return myColors
