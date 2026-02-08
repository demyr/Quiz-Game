from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_item = Question(question["text"], question["answer"])
    question_bank.append(question_item)

quiz = QuizBrain(question_bank)

while quiz.has_more_questions():
    quiz.next_question()

print("You have completed!")
print(f"Your final score is: {quiz.user_score}/{quiz.question_number}")