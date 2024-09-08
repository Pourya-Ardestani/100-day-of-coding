from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.high_score = 0
        self.read_high_score()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def read_high_score(self):
        with open("../../Desktop/high_score.txt") as file:
            content = int(file.read())
            self.high_score = content

    def update_high_score(self):
        with open("../../Desktop/high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()