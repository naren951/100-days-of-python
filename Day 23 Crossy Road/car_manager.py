import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        for _ in range(30):
            self.cars.append(self.create_car((random.randint(-270,270),random.randint(-250,250))))

    def create_car(self,position):
        super().__init__()
        car = Turtle()
        car.shape("square")
        car.penup()
        car.shapesize(stretch_len=2,stretch_wid=1)
        car.seth(180)
        car.color(random.choice(COLORS))
        car.goto(position)
        return car

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)

    def new_cars(self):
        self.cars.append(self.create_car((random.randint(310,350),random.randint(-250,250))))

