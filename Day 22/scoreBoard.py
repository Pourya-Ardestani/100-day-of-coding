from turtle import Turtle

HEIGHT = 270
FONT = "Courier"

class Writter(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.setpos(pos, HEIGHT)
        self.score = 0
        self.hideturtle()
        self.color("White")
        self.penup()
        self.write_score()

    def score_up(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(arg=self.score, align="Center", font=(FONT, 50, "bold"))
