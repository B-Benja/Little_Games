from quiz_brain import QuizBrain
from data import question_bank
from ui import QuizUI

quiz = QuizBrain(question_bank)
interface = QuizUI(quiz)

# still missing: ask user for difficulty level and no. of questions