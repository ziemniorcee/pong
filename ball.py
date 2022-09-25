from turtle import Turtle


class Ball(Turtle):
    def __init__(self, sc, lp, rp, score):
        super().__init__()
        self.screen = sc
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.left = lp
        self.right = rp
        self.scoreboard = score
        self.x = 10
        self.y = 10

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)
        self.screen.update()

        if self.collision(1) or self.collision(0):
            if self.x < 0:
                self.x -= 5
                self.y -= 1
            else:
                self.x += 5
                self.y += 1
            self.x *= -1

        if self.ycor() > 290 or self.ycor() < -290:
            self.y *= -1

    def collision(self, pad):

        if pad:
            x = self.xcor() - 10 < self.left.xcor() < self.xcor() + 10
            y = self.ycor() - 60 < self.left.ycor() < self.ycor() + 60

        else:
            x = self.xcor() - 10 < self.right.xcor() < self.xcor() + 10
            y = self.ycor() - 60 < self.right.ycor() < self.ycor() + 60
        return x and y

    def end(self):

        if self.xcor() > 390:
            self.reset_pos()
            self.scoreboard.left_score += 1

        elif self.xcor() < -390:
            self.reset_pos()
            self.scoreboard.right_score += 1
        self.scoreboard.draw_points()

    def reset_pos(self):
        if self.x < 0:
            self.x = -10
            self.y = 10
        else:
            self.x = -10
            self.y = -10
        self.goto(0, 0)
        self.x += - 1
