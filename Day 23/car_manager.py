from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5  # every level this much added to the speed of cars
FREQUENCY_RATE = 10  # down number is faster


class CarManager:
    def __init__(self):
        self.frequency = FREQUENCY_RATE
        self.listOfCars = []
        self.create_car()
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = randint(0, self.frequency)
        if random_number == 1 or random_number == 8:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.goto(300, randint(-250, 250))
            self.listOfCars.append(car)
        else:
            pass

    def move_jlo(self):
        for car in self.listOfCars:
            car.goto(car.xcor() - self.move_distance, car.ycor())

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
        self.frequency -= 1

