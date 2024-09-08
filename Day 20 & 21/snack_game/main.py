from turtle import Screen
import time
from snack import Snack
from food import Food
from scoreBoard import ScoreBoard


def screenListen():
    screen.listen()
    screen.onkey(key="Up", fun=snack.up)
    screen.onkey(key="Down", fun=snack.down)
    screen.onkey(key="Right", fun=snack.right)
    screen.onkey(key="Left", fun=snack.left)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)

snack = Snack()
food = Food()
score_board = ScoreBoard()

end = False
while not end:
    screen.update()
    time.sleep(0.1)
    snack.move()
    screenListen()
    if snack.check_wall():
        end = True
        score_board.game_over()

    if food.check_snack_reach(snack.head):
        food.change_loc()
        score_board.score += 1
        snack.get_longer()
        score_board.rewrite()

    for segment in snack.Blocks[1:]:
        if snack.head.distance(segment) < 10:
            score_board.game_over()
            end = True

screen.exitonclick()
