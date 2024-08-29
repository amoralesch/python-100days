# Turtle Crossing (Frogger)

# Re-create a simpler version of Frogger: A game where a frog (or turtle)
# needs to move from the bottom to the top, while avoiding cars, to get
# to the next level. Higher levels should be harder to complete.
#
# Again, no more new concepts, just more exercises to create a project
# from scratch.

import time
from scoreboard import Scoreboard
from turtle import Screen
from player import Player
from car_manager import CarManager

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager(WIDTH, HEIGHT)

game_is_on = True
screen.listen()
screen.onkey(player.up, 'Up')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.tick()

    if player.ycor() > (HEIGHT / 2 - 20):
        scoreboard.increase_level()
        player.return_home()
        car_manager.harder()

    if car_manager.crushed(player):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
