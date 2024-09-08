class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.count_success = 0
        self.question_list = question_bank

    # Todo 1:asking question
    def ask_question(self):
        answers = ["true", "false"]
        quest_text = self.question_list[self.question_number].text
        quest_answer = self.question_list[self.question_number].answer.lower()
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {quest_text} (True/False): ").lower()
        while user_answer not in answers:
            user_answer = input(f"try again that input was not in order (True/False): ").lower()
        self.check_q(quest_answer, user_answer)
        print(f"The correct answer was : {quest_answer}")
        print(f"your current score is: {self.count_success}/{self.question_number}.")

    # Todo 2: check if answer was correct
    def check_q(self, real, user):
        if real == user:
            self.count_success += 1
            print("you got it right")
            return True
        else:
            print("that is wrong !!")
            return False

    # Todo 3:
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
