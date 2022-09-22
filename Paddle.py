from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(-x, 0)
        self.setheading(90)
        self.shapesize(stretch_len=1)

    def up(self):
        self.setheading(90)
        x = 0
        while x < 20:
            self.forward(1)
            x += 1

    def down(self):
        self.setheading(270)
        self.forward(20)
