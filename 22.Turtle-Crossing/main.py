import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from LevelBoard import LevelBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.listen()


timmy = Player()
cars = CarManager()
level = LevelBoard()

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
        level.increase_level()
    for car in cars.cars:
        if (timmy.distance(car) < 10 and timmy.distance(car) < 10):
            game_is_on = False
            level.game_over()
screen.exitonclick()
