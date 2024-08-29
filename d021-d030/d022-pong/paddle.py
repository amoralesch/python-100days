from turtle import Turtle

DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(5, 1, 1)
        self.goto(position)

    def up(self):
        if (self.ycor() + DISTANCE) <= (self.screen.window_height() / 2 - 25):
            self.goto(self.xcor(), self.ycor() + DISTANCE)

    def down(self):
        if (self.ycor() - DISTANCE) >= -(self.screen.window_height() / 2 - 25):
            self.goto(self.xcor(), self.ycor() - DISTANCE)
