from turtle import Turtle , Screen


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def counter_clockwise():
    tim.rt(5)


def clockwise():
    tim.lt(5)


def clear_drawing():
    tim.clear()


screen = Screen()
tim = Turtle()
screen.listen()
screen.onkey(key="w" , fun=forwards)
screen.onkey(key="s" , fun=backwards)
screen.onkey(key="a" , fun=counter_clockwise)
screen.onkey(key="d" , fun=clockwise)
screen.onkey(key="c" , fun=clear_drawing)

screen.exitonclick()
