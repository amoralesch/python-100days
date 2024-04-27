# Snake Game

# Recreate the classic _Snake_ game popular on the Nokia phone.
# The game was done over 2 days, here we deal with collisions, food
# and scores.
#
# Learn about inheritance.

from turtle import Screen
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food

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

scoreboard = Scoreboard()

food = Food()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.ate_food(food):
        food.new_food()
        scoreboard.add_to_score()
        snake.grow()

    game_is_on = not snake.hit_something()

scoreboard.game_over()
screen.exitonclick()
