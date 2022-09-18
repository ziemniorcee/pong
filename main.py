from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
bg = Turtle(shape="square", visible=False)
bg.turtlesize(0.5)
bg.color("white")
bg.penup()

bg.goto(0, -280)
x = 1
while bg.ycor() < 300:
    bg.stamp()
    bg.goto(0, -280 + 40 * x)
    x += 1
screen.update()
screen.exitonclick()
