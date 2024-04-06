# Hirst Painting

# Create a painting similar to the ones from
# [Damien Hirst](https://en.wikipedia.org/wiki/Damien_Hirst).
#
# Learn about `turtle` package to start using GUI.

from turtle import Turtle, Screen
import random


def random_color():
    return random.choice(COLORS)


COLORS = [
    (35, 27, 21),
    (116, 83, 68),
    (243, 212, 190),
    (193, 154, 129),
    (17, 20, 18),
    (23, 28, 31),
    (90, 96, 102),
    (26, 19, 20),
    (145, 62, 64),
    (147, 153, 158),
    (98, 49, 41),
    (149, 154, 150),
    (235, 179, 151),
    (126, 39, 42),
    (71, 68, 48),
    (174, 106, 90),
    (173, 141, 147),
    (221, 190, 156),
    (208, 212, 210),
    (157, 126, 93)
]
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
