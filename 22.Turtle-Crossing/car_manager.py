from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.level = 1
        self.speed = STARTING_MOVE_DISTANCE

    def get_cars(self):
        chance = random.randint(1, 6)
        if chance == 6:
            color = random.randint(0, len(COLORS)-1)
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(COLORS[color])
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move_cars(self):
        for i in range(len(self.cars)):
            self.cars[i].backward(self.speed)

    def level_up_cars(self):
        self.speed += MOVE_INCREMENT
