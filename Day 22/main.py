from turtle import Screen, Turtle
from scoreBoard import Writter
import time
from rackets import Racket
from ball import Ball

MAX_SCORE = 10
SLEEP_TIME = 0.1


def dash_line():
    seperater = Turtle()
    seperater.color("white")
    seperater.penup()
    seperater.goto(0, 350)
    seperater.rt(90)
    seperater.hideturtle()
    for _ in range(35):
        seperater.pendown()
        seperater.forward(10)
        seperater.penup()
        seperater.forward(10)


def fun():
    screen.listen()
    screen.onkey(key="w", fun=Racket_2.up)
    screen.onkey(key="s", fun=Racket_2.down)
    screen.onkey(key="Up", fun=Racket_1.up)
    screen.onkey(key="Down", fun=Racket_1.down)


screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)
writer_1 = Writter(-100)
writer_2 = Writter(100)
Racket_1 = Racket(1)
Racket_2 = Racket(-1)
dash_line()
ball = Ball()

end = False
sleep_time = SLEEP_TIME
while not end:
    time.sleep(sleep_time)
    screen.update()
    ball.move()
    count = MAX_SCORE
    if Racket_1.xcor() == ball.xcor()+20 and Racket_1.distance(ball) < 70:
        ball.reflect(param1=-1)
        sleep_time *= 0.9
    elif Racket_2.xcor() == ball.xcor()-20 and Racket_2.distance(ball) < 70:
        ball.reflect(param1=-1)
        sleep_time *= 0.9
    elif ball.ycor() >= 330:
        ball.reflect(-1)
    elif ball.ycor() <= -330:
        ball.reflect(+1)
    elif ball.xcor() >= 570:
        writer_2.score_up()
        ball.restart()
    elif ball.xcor() <= -570:
        writer_1.score_up()
        ball.restart()
    fun()
    if writer_1.score >= MAX_SCORE or writer_2.score >= MAX_SCORE:
        ball.goto(0, 0)
        end = True

screen.exitonclick()
