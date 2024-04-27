from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
DISTANCE = 10
DIFFICULTY_INCREASE = 1.2


class CarManager:
    def __init__(self, width, height):
        self.cars = []
        self.x_limit = int(width / 2)
        self.y_limit = int(height / 2) - 50
        self.speed = DISTANCE

    def tick(self):
        create_car = random.randint(1, 6) <= 2
        self.move_cars()
        self.clear_cars()

        if not create_car:
            return

        y_cor = random.randint(-self.y_limit, self.y_limit)

        car = Turtle()
        car.shape('square')
        car.shapesize(1, 2, 1)
        car.penup()
        car.color(random.choice(COLORS))
        car.setposition(self.x_limit, y_cor)

        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)

    def clear_cars(self):
        for car in list(self.cars):
            if car.xcor() <= -self.x_limit:
                car.hideturtle()
                self.cars.remove(car)
            else:
                return

    def harder(self):
        self.speed *= DIFFICULTY_INCREASE

    def crushed(self, player):
        for car in self.cars:
            if car.distance(player) <= 20:
                return True

        return False
