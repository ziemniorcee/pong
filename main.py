import time
from turtle import Screen
from background import Background
from Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")

bg = Background()
bg.create_bg()
lp = Paddle(-350)
rp = Paddle(350)
scoreboard = Scoreboard()

ball = Ball(screen,lp, rp, scoreboard)

screen.update()
screen.listen()

screen.onkey(lp.up, "Up")
screen.onkey(lp.down, "Down")
screen.onkey(rp.up, "w")
screen.onkey(rp.down, "s")

game_on = True
while game_on:
    ball.move()
    ball.end()
    screen.update()
    time.sleep(0.05)

screen.exitonclick()
