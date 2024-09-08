from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    new_q = Question(item["text"], item["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.ask_question()
    print("\n")
print("you have completed the questions! ")
print(f'your final score is : {quiz.count_success} / {len(quiz.question_list)}')