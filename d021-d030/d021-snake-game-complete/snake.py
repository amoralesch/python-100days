from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DISTANCE = 21


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
            self.add_segment((0 - offset, 0))
            offset += DISTANCE

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

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
            segment.goto(previous.position())

        self.head.forward(DISTANCE)

    def ate_food(self, food):
        return self.head.distance(food) < DISTANCE

    def grow(self):
        last_segment = self.segments[-1]
        self.add_segment(last_segment.position())

    def hit_something(self):
        head = self.head
        width = (self.screen_width / 2)
        height = (self.screen_height / 2)
        hit_wall = (
            head.xcor() > width or head.xcor() < -width or
            head.ycor() > height or head.ycor() < -height
        )

        hit_self = False
        for segment in self.segments[1:]:
            if (
                int(head.xcor()) == int(segment.xcor()) and
                int(head.ycor()) == int(segment.ycor())
            ):
                hit_self = True
                break

        return hit_wall or hit_self
