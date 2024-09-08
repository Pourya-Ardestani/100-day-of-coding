from turtle import Turtle

HEIGHT = 0
WEIDTH = 550
LENGTH = 5
MOVE_DISTANCE = 15


class Racket(Turtle):
    def __init__(self, d):
        super().__init__()
        self.create_racket(d)

    def create_racket(self, d):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(d * WEIDTH, HEIGHT)

    def up(self):
        for i in range(LENGTH):
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        for i in range(LENGTH):
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
