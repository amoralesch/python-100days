# Snake Game

# Recreate the classic _Snake_ game popular on the Nokia phone.
# The game will be done over 2 days, the first one concentrating on
# creating the snake, moving, and controlling it
#
# Learn a couple of new things from _Turtle_ documentation.

from turtle import Screen
import time
from snake import Snake


WIDTH = 600
HEIGHT = 600

screen = Screen()

screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game, but Better!")
screen.tracer(0)

snake = Snake(WIDTH, HEIGHT)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    game_is_on = not snake.hit_something()

screen.exitonclick()
