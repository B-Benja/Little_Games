from turtle import Turtle
import random

CAR_SPEED = 5


class Cars():

    def __init__(self):
        self.all_cars = []
        self.car_speed = CAR_SPEED

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    def random_spawn(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random_y = random.randint(-260, 300)
            new_car = Turtle("square")
            new_car.penup()
            new_car.sety(random_y)
            new_car.setx(340)
            new_car.fillcolor(self.random_color())
            new_car.shapesize(1, 2, 1)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_forward(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += 10

