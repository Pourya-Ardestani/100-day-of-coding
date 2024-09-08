from turtle import Turtle, Screen
from random import choice
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
screen = Screen()
screen.setup(height=400, width=500)
user = screen.textinput("make a bet", "select one of the turtles Enter color:" )

listOfTurtles = []
count = 0
for item in colors:
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(item)
    tim.goto(-230, -100+count*40)
    count += 1
    listOfTurtles.append(tim)

random_nums = [0, 2, 5, 8, 7, 9, 10, 12, 15]
winner_color = ''
end = False
while not end:
    for turtle in listOfTurtles:
        turtle.fd(choice(random_nums))
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            end = True
            if user == winner_color:
                print(f"you won , the winner turtle is a {winner_color} turtle")
            else:
                print(f"you lose , the winner turtle is a {winner_color} turtle")


screen.title(winner_color+" has wons !!!")


screen.exitonclick()