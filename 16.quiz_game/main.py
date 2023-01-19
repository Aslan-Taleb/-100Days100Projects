from question_model import Question
from data import question_data
from quiz_brain import *

import os

question_bank = []
question_bank = []
for question in question_data:
    question = Question(question["question"], question["correct_answer"])
    question_bank.append(question)


def main():
    print(logo)
    the_quiz = QuizBrain(question_bank)
    while the_quiz.still_has_question():
        answer = the_quiz.next_question()
        if the_quiz.test_answer(answer):
            the_quiz.score(answer)
    the_quiz.logo_print()
    test = input(
        "Another Time ? (yeah it's the same question for now.) (y/n) : ")
    if test == 'y':
        return False
    else:
        return True


while not main():
    os.system('cls')
    main()
print("Goodbye!")
