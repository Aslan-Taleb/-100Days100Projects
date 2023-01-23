from turtle import Turtle

FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.score_max = self.read_file_score()
        self.update_scoreboard()
        self.print_max_score()

    def update_scoreboard(self):
        self.goto(0, 280)
        self.write(f"Score : {self.score}", align="center",
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        self.print_max_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align="center",
                   font=FONT)

    def read_file_score(self):
        file = open('score_max.txt', "r")
        score_in_the_file = file.read()
        if score_in_the_file == '':
            score_in_the_file = 0
        file.close()
        return int(score_in_the_file)

    def print_max_score(self):
        self.goto(200, 280)
        self.update_max_score()
        self.write(f"Highest Score : {self.score_max}", align="center",
                   font=FONT)

    def update_max_score(self):
        if self.score_max <= self.score:
            self.score_max = self.score
            self.update_file_score()

    def update_file_score(self):
        file = open('score_max.txt', "w")
        file.write(str(self.score_max))
        file.close()
