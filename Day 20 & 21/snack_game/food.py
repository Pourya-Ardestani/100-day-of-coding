from turtle import Turtle
from random import randint

NEXT_TO = 17


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("Red")
        self.speed("fastest")
        self.change_loc()

    def change_loc(self):
        self.goto(randint(-280, 280), randint(-280, 280))

    def check_snack_reach(self, head):
        if self.xcor() - NEXT_TO < head.xcor() < self.xcor() + NEXT_TO and\
                self.ycor() - NEXT_TO < head.ycor() < self.ycor() + NEXT_TO:
            return True
        return False
