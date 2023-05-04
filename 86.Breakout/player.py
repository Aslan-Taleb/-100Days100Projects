from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos = 0
        self.y_pos = -350
        self.height = 5
        self.my_color = "grey"
        self.create_player()

    def create_player(self):
        self.shape("square")
        self.color(self.my_color)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.speed("fastest")
        self.goto(self.x_pos, self.y_pos)

    def move_to(self, x):
        self.x_pos = x
        self.goto(x, self.y_pos)

    def reset_player(self):
        self.x_pos = 0
        self.y_pos = -350
        self.goto(self.x_pos, self.y_pos)

    def right(self):
        if self.x_pos <= 640:
            self.x_pos += 40
            self.goto(self.x_pos, self.y_pos)

    def left(self):
        if self.x_pos >= -640:
            self.x_pos -= 40
            self.goto(self.x_pos, self.y_pos)
