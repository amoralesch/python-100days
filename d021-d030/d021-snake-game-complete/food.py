from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('blue')
        self.penup()
        self.x_value = int(self.screen.window_width() / 2) - 20
        self.y_value = int(self.screen.window_height() / 2) - 20
        self.new_food()

    def new_food(self):
        x = random.randint(0, self.x_value)
        y = random.randint(0, self.y_value)
        self.goto(x, y)
        self.circle(10)
