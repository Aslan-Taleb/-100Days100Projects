import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


timmy = Player()
cars = CarManager()

screen.onkey(timmy.move, "Up")
screen.onkey(timmy.move, "space")
screen.onkey(timmy.move, "z")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.get_cars()
    cars.move_cars()
    if timmy.ycor() > 280:
        timmy.level_up()
        cars.level_up_cars()
