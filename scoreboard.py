from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.color("white")

    def draw_points(self):
        self.clear()
        self.goto(-40, 250)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(40, 250)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)
