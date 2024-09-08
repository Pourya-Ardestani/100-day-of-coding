import turtle
from random import choice, randint
from turtle import Turtle, Screen

# import colorgram
# colors = colorgram.extract('image.jpg', 30)
#
# list_tuples = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color_tuple = (r, g, b)
#     list_tuples.append(color_tuple)
# print(list_tuples)
# import colorgram
# list_tuple = []
# colors = colorgram.extract("image1.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple_colors = (r, g, b)
#     list_tuple.append(tuple_colors)
# print(list_tuple)

list_tuple = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
list_tuples = [(188, 74, 20), (56, 34, 13), (149, 26, 9), (237, 226, 77), (24, 31, 60), (113, 167, 210), (45, 85, 143),
               (227, 243, 238), (217, 154, 82), (34, 50, 124), (191, 144, 25), (26, 51, 29), (201, 93, 126),
               (242, 214, 6), (250, 244, 249), (119, 35, 51), (120, 187, 149), (55, 129, 74), (70, 82, 17),
               (36, 84, 40), (142, 51, 58), (74, 128, 200), (205, 86, 62), (82, 31, 44), (104, 180, 70),
               (148, 204, 223), (197, 120, 162), (23, 77, 100)]

turtle.colormode(255)
screen = Screen()
tim = Turtle()

list_of_colors = ["red", "yellow", "blue", "green", "gold", "brown", "cyan", "black", "orange"]

dir = ["right", "left", "back", "forward"]



def squer():
    for _ in range(4):
        tim.forward(100)
        tim.left(90)


def dashed_line():
    for _ in range(15):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)


def draw_shape(n):
    angle = 180 - ((n - 2) * 180) / n
    for _ in range(n):
        tim.forward(100)
        tim.right(angle)


def move(direct):
    if direct == "right":
        tim.right(90)
    elif direct == "left":
        tim.left(90),
    elif direct == "back":
        tim.rt(180),
    elif direct == "forward":
        pass


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def brain_move():
    for _ in range(200):
        # directions[choice(dir)]
        move(choice(dir))
        # tim.color(choice(list_of_colors))
        tim.color(random_color())
        tim.fd(20)


def doted_line():
    for _ in range(10):
        # tim.dot(20, choice(list_tuple))
        tim.dot(20, choice(list_tuples))
        tim.fd(50)


tim.penup()
# tim.right(135)
# tim.fd(320)
# tim.lt(135)
tim.speed("fastest")
tim.goto(-226, -226)
currentX = tim.xcor()
currentY = tim.ycor()

for i in range(10):
    tim.goto(currentX, currentY+i*50)
    doted_line()
tim.hideturtle()
# print(list_tuples)
# n = 100
# angle = 0
# for i in range(n):
#     U = 360 / n
#     angle += U
#     tim.setheading(angle)
#     tim.circle(100)
#     tim.color(random_color())



# tim.pensize(10)
# brain_move()

#dashed_line()
# tim.lt(90)
# print(tim.speed())
# print(tim.speed())
# dashed_line()




# for n in range(3, 11):
#     draw_shape(n)
#     tim.color(list_of_colors[n - 3])

screen.exitonclick()
