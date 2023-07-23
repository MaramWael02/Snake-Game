from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.goto(x=0, y=260)
        self.clear()
        self.write(f"Score = {self.score}", align="center", move=False, font=("sunrise international", 15, "bold"))

    def increase_score(self):
        self.score += 1
        self.display_score()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", move=False, font=("sunrise international", 15, "bold"))
