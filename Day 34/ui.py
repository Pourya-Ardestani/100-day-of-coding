from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.window.title("quizzer")
        self.score_label = Label(text=f'Score: {self.quiz.score}',
                                 background=THEME_COLOR, fg='white',
                                 font=('Arial', 12,))
        self.score_label.grid(column=1, row=0, pady=10)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question = self.canvas.create_text(150, 125,
                                                text="bayad avaz she ",
                                                font=('Arial', 20, 'italic'),
                                                fill=THEME_COLOR,
                                                width=280
                                                )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10)

        # buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, command=self.click_true, highlightthickness=0)
        self.false_button = Button(image=false_img, command=self.click_false, highlightthickness=0)
        self.true_button.grid(column=0, row=2, padx=45, pady=40)
        self.false_button.grid(column=1, row=2, padx=45, pady=40)

        self.get_next_question()

        self.window.mainloop()

    def click_true(self):
        answer_is_right = self.quiz.check_answer(user_answer='True')
        self.is_right(answer_is_right)

    def click_false(self):
        answer_is_right = self.quiz.check_answer(user_answer='False')
        self.is_right(answer_is_right)

    def get_next_question(self):
        if self.quiz.still_has_questions():
            new_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=new_question)
        else:
            self.canvas.itemconfig(self.question, text="no more questions")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def is_right(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(500, self.back_to_theme)
        self.get_next_question()
        self.update_score()

    def back_to_theme(self):
        self.canvas.config(bg='white')

    def update_score(self):
        self.score_label.config(text=f'Score: {self.quiz.score}')
