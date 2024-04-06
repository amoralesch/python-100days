# Hirst Painting

# Create a painting similar to the ones from
# [Damien Hirst](https://en.wikipedia.org/wiki/Damien_Hirst).
#
# Learn about `turtle` package to start using GUI.

from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


RATIO = 20
GAP = 35
ROWS = 15
COLUMNS = 15
X_ORIGIN = - int((COLUMNS - 1) * GAP / 2)
Y_ORIGIN = int((ROWS - 1) * GAP / 2)

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.speed("fastest")

for row in range(ROWS):
    for column in range(COLUMNS):
        turtle.teleport(X_ORIGIN + GAP * column, Y_ORIGIN - GAP * row)

        turtle.pencolor(random_color())
        turtle.dot(RATIO)

screen.exitonclick()
