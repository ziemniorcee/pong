from turtle import Turtle

POSITIONS = [(-380, -30), (-380, -20), (-380, -10), (-380, 0), (-380, 10), (-380, 20), (-380, 30)]
UP = 90
DOWN = 270
MOVE = 20
xd = Turtle()


class LeftPaddle:
    def __init__(self):
        super().__init__()
        self.segments = []

    def create(self):
        for position in POSITIONS:
            new_segment = Turtle("square")
            new_segment.turtlesize(0.5)
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def up(self):
        for segment in self.segments:
            segment.setheading(UP)
            segment.forward(MOVE)

    def down(self):
        for segment in self.segments:
            segment.setheading(DOWN)
            segment.forward(MOVE)
