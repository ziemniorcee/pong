from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self, sc, lp, rp):
        super().__init__()
        self.screen = sc
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.left = lp
        self.right = rp
        self.setheading(180)
        self.x = 10
        self.y = 10

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)
        self.screen.update()
        if self.xcor() > 0:
            if self.collision(1):
                self.x *= -1
        else:
            if self.collision(0):
                self.x *= -1
        self.wall()

    def wall(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.y *= -1

    def collision(self, pad):
        if pad:
            x = self.xcor() - 10 < self.left.xcor() < self.xcor() + 10
            y = self.ycor() - 50 < self.left.ycor() < self.ycor() + 50
        else:
            x = self.xcor() - 10 < self.right.xcor() < self.xcor() + 10
            y = self.ycor() - 50 < self.right.ycor() < self.ycor() + 50
        return x and y
