from turtle import Turtle
import random
import time
COLORS = ["#FF1493", "red", "orange", "yellow",
          "green", "blue", "purple", "cyan"]
INITIAL_BRICK_POSITION_X = -715
INITIAL_BRICK_POSITION_Y = 300


class Blocks():
    def __init__(self):
        self.list_blocks = []
        self.x_pos = INITIAL_BRICK_POSITION_X
        self.y_pos = INITIAL_BRICK_POSITION_Y

    def get_block(self, color):
        block = Turtle()
        block.shape("square")
        block.fillcolor('#ffffff')
        block.shapesize(stretch_wid=0.75, stretch_len=3)
        block.color(COLORS[color])
        block.penup()
        block.goto(self.x_pos, self.y_pos)
        self.list_blocks.append(block)

    def add_blocks(self):
        for j in range(0, 8):
            for i in range(0, 21):
                self.x_pos += 65
                self.get_block(j)
            self.x_pos = INITIAL_BRICK_POSITION_X
            self.y_pos -= 20

    def reset_blocks(self):
        for i in self.list_blocks:
            i.clear()
            i.hideturtle()
        self.list_blocks = []
        self.x_pos = INITIAL_BRICK_POSITION_X
        self.y_pos = INITIAL_BRICK_POSITION_Y
        self.add_blocks()
