from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed("slow")
        self.zx = 1
        self.zy = 1

    def move(self):
        self.goto(self.xcor() + (self.zx * 10), self.ycor() + (self.zy * 10))

    def restart(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.zx *= -1

    def reflect(self, param=1, param1=1):
        self.zy *= param
        self.zx *= param1
