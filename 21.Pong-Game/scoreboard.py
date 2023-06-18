from turtle import Turtle

FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self, l_r):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(l_r, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align="center",
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
