import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_column = data["state"]
states = states_column.tolist()
answered_before = []
# print(states)
end = False
second_turtle = turtle.Turtle()
second_turtle.hideturtle()


def write_state_name():
    second_turtle.penup()
    second_turtle.goto(int(data_row['x']), int(data_row['y']))
    second_turtle.write(answer)


def create_nonTyped_state_file():
    # state_to_learn = []
    # for state in states:
    #     if state not in answered_before:
    #         state_to_learn.append(state)
    # TODO using list comprehensions instead of code above from day 26

    state_to_learn = [state for state in states if state not in answered_before]
    state_to_learn_df = pandas.DataFrame(state_to_learn)
    state_to_learn_df.to_csv("Missing_states.csv")


while len(answered_before) < 50:
    answer = screen.textinput(title=f"{len(answered_before)}/50 the State",
                              prompt="What's another state's name? ").title()
    if answer == "Exit":
        break

    if answer in states:
        if answer not in answered_before:
            answered_before.append(answer)
            data_row = data[data['state'] == answer]
            write_state_name()

create_nonTyped_state_file()
screen.exitonclick()
