from turtle import Turtle

FONT = ('Courier', 20, 'normal')


class Score_lives(Turtle):
    def __init__(self, x):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.x = x
        self.penup()
        self.goto(self.x, 350)
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        if self.x < 0:
            self.write(f"SCORE : {self.score}", align="center",
                       font=FONT)
        else:
            self.write(f"LIVES : {self.lives}", align="center",
                       font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.clear()
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.clear()
        self.update_scoreboard()

    def reset_lives(self):
        self.lives = 3
        self.clear()
        self.update_scoreboard()
