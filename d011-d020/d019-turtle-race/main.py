# Turtle Race

# Create a simple game where a user can pick a turtle by its color,
# and see if it wins the race.
#
# Learn about multiple objects of the same class, and more methods
# from the Turtle library.

from turtle import Turtle, Screen
import random


def new_turtle(clr, y_pos):
    the_turtle = Turtle(shape="turtle")
    the_turtle.penup()
    the_turtle.color(clr)
    the_turtle.goto(START_POSITION, y_pos)

    return the_turtle


def move_turtle(the_turtle):
    distance = random.randint(0, MAX_DISTANCE)
    the_turtle.forward(distance)


def turtle_finished(the_turtle):
    return (the_turtle.xcor() + TURTLE_WIDTH / 2) > (SCREEN_WIDTH / 2)


COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
TURTLE_WIDTH = 40
GAP = 60
MAX_DISTANCE = 10
START_POSITION = -(SCREEN_WIDTH / 2) + TURTLE_WIDTH / 2

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

user_option = screen.textinput(
    "Make a bet",
    "Pick the color of the winner turtle. "
    f"{COLORS}: ")

y_offset = 150
turtles = []

for color in COLORS:
    turtles.append(new_turtle(color, y_offset))
    y_offset -= GAP

winner_turtle = None
is_race_on = True
while is_race_on:
    for turtle in turtles:
        move_turtle(turtle)

        if turtle_finished(turtle):
            winner_turtle = turtle.pencolor()
            is_race_on = False
            break

if user_option == winner_turtle:
    print("You've won!")
else:
    print(f"You've lost, the winner turtle was {winner_turtle}")

screen.exitonclick()
