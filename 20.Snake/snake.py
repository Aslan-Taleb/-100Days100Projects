from turtle import Turtle
MOVE_DISTANCE = 20
FONT = ('Courier', 12, 'normal')


class Snake:
    def __init__(self):
        self.snake = []
        self.number_part_snake = 3
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for _ in range(self.number_part_snake):
            self.add_segment()

    def add_segment(self):
        stick = 20
        part_snake = Turtle(shape="square")
        part_snake.color("white")
        part_snake.penup()
        part_snake.speed("fastest")
        if len(self.snake) > 0:
            part_snake.goto(self.snake[len(
                self.snake)-1].xcor()-stick, self.snake[len(self.snake)-1].ycor()-stick)
        else:
            part_snake.goto(0, 0)
        self.snake.append(part_snake)

    def snake_extend(self):
        self.number_part_snake += 1
        self.add_segment()

    def push_snake(self):
        # for seg_snake in range(start=len(snake)-1, stop=0, step=-1):
        for seg_snake in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[seg_snake-1].xcor()
            new_y = self.snake[seg_snake-1].ycor()
            self.snake[seg_snake].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
