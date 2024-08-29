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
RATIO = 10
GAP = 30
ROWS = 20
COLUMNS = 21
X_ORIGIN = - int((COLUMNS - 1) * GAP / 2)
Y_ORIGIN = int((ROWS - 1) * GAP / 2)

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()

turtle.teleport(X_ORIGIN - GAP, Y_ORIGIN)

x_print = COLUMNS
y_print = ROWS - 1

while x_print > 0 or y_print > 0:
    if y_print >= 0:
        for i in range(x_print):
            turtle.forward(GAP)
            turtle.dot(RATIO, random_color())
    else:
        x_print = 0

    turtle.right(90)

    if x_print >= 0:
        for i in range(y_print):
            turtle.forward(GAP)
            turtle.dot(RATIO, random_color())
    else:
        y_print = 0

    turtle.right(90)

    x_print -= 1
    y_print -= 1

screen.exitonclick()
