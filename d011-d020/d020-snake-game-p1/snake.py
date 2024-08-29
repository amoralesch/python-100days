from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DISTANCE = 20


class Snake:

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.segments = []
        self.new_snake()
        self.head = self.segments[0]

    def new_snake(self):
        offset = 0

        for i in range(0, 3):
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(0 - offset, 0)
            self.segments.append(segment)
            offset += 20

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            segment = self.segments[i]
            previous = self.segments[i - 1]
            segment.goto(previous.xcor(), previous.ycor())

        self.head.forward(DISTANCE)

    def hit_something(self):
        head = self.head
        hit_wall = head.xcor() > self.screen_width / 2 or \
                   head.xcor() < -(self.screen_width / 2) or \
                   head.ycor() > self.screen_height / 2 or \
                   head.ycor() < -(self.screen_height / 2)

        return hit_wall
