import random


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self, previous_questions):
        current_question = self.question_list[random.randint(0, len(self.question_list)-1)]
        previous_questions.append(current_question)
        if current_question in previous_questions:
            pass
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: Category: {current_question.category} \n"
                            f" {current_question.text}"
                            f"\n (True/False):")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self, long):
        return self.question_number < long

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
