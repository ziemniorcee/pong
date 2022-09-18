from turtle import Screen, Turtle
from background import Background

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")

bg = Background()
bg.create_bg()
screen.update()

screen.exitonclick()

