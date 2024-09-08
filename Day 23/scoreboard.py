from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 265)
        self.level = 1
        self.write_level()

    def write_level(self):
        self.write(arg=f"LEVEL: {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER !", align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write_level()


def dash_line(turtle):
    turtle.penup()
    turtle.goto(-280, 250)
    turtle.setheading(0)
    for _ in range(60):
        turtle.pendown()
        turtle.fd(10)
        turtle.penup()
        turtle.fd(10)
    turtle.penup()