# Quiz Game - API version

# Redo the quiz game (from day 17), but make it consume an API, and
# also have a GUI.
#
# Practice with APIs, and tkinter

from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from random import shuffle
import ui

question_bank = [Question(q['question'], q['correct_answer']) for q in question_data]
shuffle(question_bank)
quiz_brain = QuizBrain(question_bank)
ui = ui.QuizUi(quiz_brain)
