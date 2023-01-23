from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pos_x = STARTING_POSITION[0]
        self.pos_y = STARTING_POSITION[1]
        self.setheading(90)
        self.penup()
        self.goto(self.pos_x, self.pos_y)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.pos_x = STARTING_POSITION[0]
        self.pos_y = STARTING_POSITION[1]
        self.goto(self.pos_x, self.pos_y)
