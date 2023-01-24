from turtle import Turtle

FONT = ('Courier', 12, 'normal')


class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 1
        self.update_LevelBoard()

    def update_LevelBoard(self):
        self.goto(-250, 280)
        self.write(f"Level : {self.level}", align="center",
                   font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_LevelBoard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align="center",
                   font=FONT)
