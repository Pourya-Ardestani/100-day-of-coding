from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT = ('Arial', 60, "bold")
LANGUAGE_TO_LEARN = "French"
current_word = {}

# TODO exception by file errors
try:
    data = pandas.read_csv("data/to_learn_word.cvs")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
try:
    learned_words_df = pandas.read_csv("data/learned_words.csv")
except FileNotFoundError:
    learned_words = []
else:
    learned_words = learned_words_df.to_dict(orient="records")


def delete_and_next_word():
    global to_learn, learned_words
    # learned_words.insert(0,current_word)
    learned_words.append(current_word)
    try:
        to_learn.remove(current_word)
        to_learn_df = pandas.DataFrame(to_learn)
        to_learn_df.to_csv("data/to_learn_word.cvs", index=False)
    except ValueError:
        canvas.itemconfig(card_title, text="Words has ended")
        canvas.itemconfig(card_word, text=' ')
    else:
        learned_df = pandas.DataFrame(learned_words)
        learned_df.to_csv("data/learned_words.csv", index=False)
        next_word()


def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_word = choice(to_learn)
    except IndexError:
        canvas.itemconfig(card_title, text="Words has ended")
        canvas.itemconfig(card_word, text=' ')
    else:
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_word["French"], fill="black")
        canvas.itemconfig(card_bg, image=card_front_image)
        flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_image)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# TODO Cards:
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

# TODO Titles:
card_title = canvas.create_text(400, 100, text="", font=('Arial', 40, "italic"))
card_word = canvas.create_text(400, 265, text="", font=FONT)

next_word()
# TODO Buttons:
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, command=next_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, command=delete_and_next_word)
right_button.grid(column=1, row=1)

window.mainloop()
