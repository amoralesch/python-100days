from turtle import Turtle

DISTANCE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.return_home()

    def up(self):
        self.forward(DISTANCE)

    def return_home(self):
        self.goto(0, -(self.screen.window_height() / 2) + 20)
