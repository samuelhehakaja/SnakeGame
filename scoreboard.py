from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", "16", "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.add_score(0)

    def add_score(self, score):
        self.clear()
        self.write(f"Score: {score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)