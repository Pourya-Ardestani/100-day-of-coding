from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    window.after_cancel(timer)
    check_label.config(text='')
    title_label.config(text="Timer", font=(FONT_NAME, 40), foreground=GREEN, background=YELLOW)
    canvas.itemconfig(countdown_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_command():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        if reps % 7 == 0:
            count_down(long_break_sec)
            title_label.config(text="Long break", foreground=RED)
        else:
            count_down(short_break_sec)
            title_label.config(text="Short break", foreground=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Focus", foreground=GREEN)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(countdown_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_command()
        # check_mark_count = math.floor(reps / 2)
        # if reps % 2 == 1:
        #     check_label.config(text=check_mark_count * "✔️")
        marks = ''
        for _ in range(math.floor(reps / 2)):
            marks += "✔️"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")  # tomato in italian
window.config(padx=100, pady=50, background=YELLOW)
second_count = 60

# button start
button_start = Button(text="Start", width=10, highlightthickness=0, command=start_command)  # need command
button_start.grid(column=0, row=2)

# button Reset
button_Reset = Button(text="Reset", width=10, highlightthickness=0, command=reset)
button_Reset.grid(column=2, row=2)

# Label Timer
title_label = Label(text="Timer", font=(FONT_NAME, 40), foreground=GREEN, background=YELLOW)
title_label.grid(column=1, row=0)

# check_mark
check_label = Label(text=" ", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 10, "bold"))
check_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=233, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=tomato_img)
countdown_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()