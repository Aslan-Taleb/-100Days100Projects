from library import *


print("Welcome To Etch A Sketch")
screen = Screen()
colormode(255)
screen.title("Etch A Scketch")
screen.bgcolor(211, 211, 211)

tuto()
screen.listen()
screen.onkeypress(key="Up", fun=move_forward)
screen.onkeypress(key="Left", fun=move_left)
screen.onkeypress(key="Down", fun=move_backward)
screen.onkeypress(key="Right", fun=move_right)
screen.onkey(key="c", fun=reset)
x = screen.ontimer(fun=tuto, t=1)


screen.exitonclick()
