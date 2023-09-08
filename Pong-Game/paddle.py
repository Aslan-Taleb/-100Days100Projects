from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = 0
        self.height = 5
        self.my_color = "white"
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color(self.my_color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(self.x_pos, self.y_pos)

    def up(self):
        if self.y_pos <= 250:
            self.y_pos += 20 * 2
            self.goto(self.x_pos, self.y_pos)

    def down(self):
        if self.y_pos >= -220:
            self.y_pos -= 20 * 2
            self.goto(self.x_pos, self.y_pos)
