from turtle import *
import colorgram as c


def color_generate(image):
    colors = c.extract(image, 35)
    myColors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        myColors.append((r, g, b))
    return myColors
