# Quiz Game

# Create a game that shows facts to the user, and they have to answer
# if they fact is true or false.

# Concepts to learn include how to declare classes and create objects

from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from etc.helpers import ask_input
from random import shuffle


def is_valid_option(value):
    return value.strip().lower() in ['true', 'false']


question_bank = []

for q in question_data:
    question_bank.append(Question(q['question'], q['correct_answer']))

shuffle(question_bank)
quiz_brain = QuizBrain(question_bank)

print('Welcome to Quiz Game!')

while quiz_brain.has_more_questions():
    question = quiz_brain.next_question()
    answer = ask_input(
        f'{question.prompt()} (true/false): ',
        is_valid_option).lower()
    quiz_brain.answer(answer)

print(
    'You finished the quiz. '
    f'Your final score is {quiz_brain.score}/{quiz_brain.total_questions()}')
