from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(-x, 0)
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.speed("fastest")

    def up(self):
        self.setheading(90)
        self.forward(40)

    def down(self):
        self.setheading(270)
        self.forward(40)
