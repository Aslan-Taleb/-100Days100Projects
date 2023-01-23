from turtle import Turtle


class Line(Turtle):
    def __init__(self, y_pos):
        super().__init__()
        self.x_pos = 0
        self.y_pos = y_pos
        self.height = 2
        self.my_color = "white"
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color(self.my_color)
        self.shapesize(stretch_wid=2, stretch_len=0.2)
        self.penup()
        self.goto(self.x_pos, self.y_pos)
