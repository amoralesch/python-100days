from turtle import Turtle

DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_delta = 1
        self.y_delta = 1
        self.the_speed = 1

    def move(self):
        x = self.xcor() + (self.x_delta * DISTANCE)
        y = self.ycor() + (self.y_delta * DISTANCE)
        self.goto(x, y)

    def bounce(self):
        if self.ycor() > 0:
            self.y_delta = -1
        else:
            self.y_delta = 1

    def reflect(self):
        self.the_speed *= 0.9

        if self.xcor() > 0:
            self.x_delta = -1
        else:
            self.x_delta = 1

    def restart(self):
        self.the_speed = 1
        self.reflect()
        self.home()

    def speed_factor(self):
        return self.the_speed
