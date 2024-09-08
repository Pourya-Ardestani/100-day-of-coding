from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color("white")
        self.rewrite()
        self.hideturtle()

    def rewrite(self):
        self.clear()
        self.write(arg=f"Score:  {self.score}", align="center", font=("Courier", 14, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over !!", align="center", font=("Arial", 24, "bold"))
