from tkinter import Button, Canvas, Label, PhotoImage, Tk
from Screen import *


def main():

    with open("wpm.txt") as data:
        high_score = int(data.read())
    screen = Screen(high_score)


main()
