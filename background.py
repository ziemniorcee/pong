from turtle import Turtle


class Background(Turtle):
    def __init__(self):
        super().__init__()
        self.bg = Turtle(shape="square", visible=False)
        self.bg.turtlesize(0.5)
        self.bg.color("white")
        self.bg.penup()
        self.bg.goto(0, -280)

    def create_bg(self):
        x = 1
        while self.bg.ycor() < 300:
            self.bg.stamp()
            self.bg.goto(0, -280 + 40 * x)
            x += 1
