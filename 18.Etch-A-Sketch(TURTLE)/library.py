from turtle import *
import time


def move_forward():
    forward(10)


def move_backward():
    bk(10)


def move_left():
    left(10)


def move_right():
    right(10)


def tuto():
    startTime = time.time()
    hideturtle()
    write("Welcome to the Game 'Etch A Sketch' !\n'↑' Forward;\n'→' Right;\n'←' Left;\n'↓' Backward;\n'c' Clear;",
          False, align="center", font=('Arial', 20, 'normal'))
    while time.time() - startTime < 2:
        pass

    clear()
    showturtle()
    return 0
