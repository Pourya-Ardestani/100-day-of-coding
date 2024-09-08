import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, dash_line


def crash():
    for car in carManager.listOfCars:
        if player.distance(car.pos()) < 22:
            return True


def move():
    screen.listen()
    screen.onkey(key="w", fun=player.move_up)
    screen.onkey(key="a", fun=player.move_left)
    screen.onkey(key="d", fun=player.move_right)


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
end = False
carManager = CarManager()
score = Scoreboard()
dash_liner = Turtle()
dash_line(dash_liner)

while not end:
    time.sleep(0.1)
    screen.update()
    move()
    carManager.create_car()
    carManager.move_jlo()
    if crash():
        end = True
        score.game_over()

    elif player.ycor() > 240:
        score.level_up()
        player.goto(0, -280)
        carManager.level_up()

screen.exitonclick()

