from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from turtle import Screen


def Game():
    screen = Screen()
    screen.title("Snake")
    screen.tracer(0)
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.colormode(255)
    screen.listen()
    mySnake = Snake()

    myFood = Food()
    myScoreboard = Scoreboard()

    screen.onkey(mySnake.up, "Up")
    screen.onkey(mySnake.down, "Down")
    screen.onkey(mySnake.left, "Left")
    screen.onkey(mySnake.right, "Right")
    screen.onkey(mySnake.up, "z")
    screen.onkey(mySnake.down, "s")
    screen.onkey(mySnake.left, "q")
    screen.onkey(mySnake.right, "d")
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.05)
        mySnake.push_snake()

        # detect collisions food and snake
        if mySnake.head.distance(myFood) < 15:
            myFood.refresh()
            mySnake.snake_extend()
            myScoreboard.increase_score()

        # Detect collision with wall.
        if mySnake.head.xcor() > 290 or mySnake.head.xcor() < -290 or mySnake.head.ycor() > 290 or mySnake.head.ycor() < -290:
            game_is_on = False
            myScoreboard.game_over()

        # Game Over Snake Tail
        for tail in mySnake.snake[1:]:
            if mySnake.head.distance(tail) < 10:
                game_is_on = False
                myScoreboard.game_over()
    screen.exitonclick()


Game()
