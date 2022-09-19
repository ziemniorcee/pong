import time
from turtle import Screen
from background import Background
from LeftPaddle import LeftPaddle

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")

bg = Background()
bg.create_bg()
lp = LeftPaddle()
lp.create()
screen.update()
screen.listen()

screen.onkey(lp.up, "Up")
screen.onkey(lp.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()

