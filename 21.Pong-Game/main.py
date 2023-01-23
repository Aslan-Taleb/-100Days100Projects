from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from line import Line


screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

y_up = -265
for i in range(12):
    line = Line(y_up)
    y_up += 50

r_pad = Paddle(350)
l_pad = Paddle(-350)

ball = Ball()
r_score = Scoreboard(100)
l_score = Scoreboard(-100)

screen.onkey(r_pad.up, "Up")
screen.onkey(r_pad.down, "Down")
screen.onkey(l_pad.up, "z")
screen.onkey(l_pad.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.mySpeed)
    ball.move_ball()
    # contact ball paddle
    if (ball.distance(r_pad) < 50 and ball.xcor() > 320) or (ball.distance(l_pad) < 50 and ball.xcor() < -320):
        ball.bounce_ball_contact()
        ball.increase_speed()
    # ball out right
    if ball.xcor() >= 380:
        ball.ball_reset()
        l_score.increase_score()

    # ball out left
    if ball.xcor() <= -380:
        ball.ball_reset()
        r_score.increase_score()


screen.exitonclick()
