# Pong Game

# Another game to create using _turtle_ library.
#
# No new concepts, just more practice with making projects from zero.

from turtle import Screen
import time
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

WIDTH = 600
HEIGHT = 400
MARGIN = 10
Y_OUTSIDE = HEIGHT / 2 - MARGIN
X_OUTSIDE = WIDTH / 2 - MARGIN

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.tracer(0)

scoreboard = Scoreboard()

r_paddle = Paddle((WIDTH / 2 - 50, 0))
l_paddle = Paddle((-WIDTH / 2 + 50, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1 * ball.speed_factor())
    ball.move()
    hit_r_paddle = ball.distance(r_paddle) < 50 and ball.xcor() >= X_OUTSIDE - 60
    hit_l_paddle = ball.distance(l_paddle) < 50 and ball.xcor() <= -X_OUTSIDE + 60

    if ball.ycor() >= Y_OUTSIDE or ball.ycor() <= -Y_OUTSIDE:
        ball.bounce()

    if hit_r_paddle or hit_l_paddle:
        ball.reflect()

    if ball.xcor() > X_OUTSIDE:
        scoreboard.l_point()
        ball.restart()

    if ball.xcor() < -X_OUTSIDE:
        scoreboard.r_point()
        ball.restart()

    is_game_on = not scoreboard.is_game_over()

screen.exitonclick()
