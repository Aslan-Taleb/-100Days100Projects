from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos = 0
        self.y_pos = 0
        self.my_direction_x = 10
        self.my_direction_y = 10
        self.create_ball()
        self.mySpeed = 0.05

    def create_ball(self):
        self.goto(self.x_pos, self.y_pos)
        self.shape("circle")
        self.penup()
        self.color(135, 206, 250)
        self.speed("fastest")

    def move_ball(self):
        if self.y_pos <= 280 and self.y_pos >= -280:
            self.x_pos += self.my_direction_x
            self.y_pos += self.my_direction_y
            self.goto(self.x_pos, self.y_pos)

        else:
            self.bounce_ball()

    def bounce_ball(self):
        self.my_direction_y = -(self.my_direction_y)
        self.x_pos += self.my_direction_x
        self.y_pos += self.my_direction_y
        self.goto(self.x_pos, self.y_pos)

    def bounce_ball_contact(self):

        self.my_direction_x = -(self.my_direction_x)
        self.increase_speed()
        self.move_ball()

    def ball_reset(self):
        self.x_pos = 0
        self.y_pos = 0
        self.reset_speed()
        self.my_direction_x *= -1
        self.my_direction_x = self.my_direction_x
        self.create_ball()

    def increase_speed(self):
        self.mySpeed *= 0.9

    def reset_speed(self):
        self.mySpeed = 0.05
