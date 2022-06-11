from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
previous_questions = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_category = question["category"]
    question_difficulty = question["difficulty"]
    new_question = Question(q_text=question_text, q_answer=question_answer, q_category=question_category,
                            q_difficulty=question_difficulty)
    question_bank.append(new_question)

while True:
    quiz = QuizBrain(question_bank)
    long = int(input("How many questions would you like to answer?: "))
    if long > len(question_bank):
        print("Not enough questions, try entering fewer.")
        continue

    while quiz.still_has_questions(long):
        quiz.next_question(previous_questions)
    break

print("You've completed the quiz")
print(f"Your final score was:{quiz.score}/{quiz.question_number}")
print("\n")
