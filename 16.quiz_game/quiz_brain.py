from art import *


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.the_score = 0

    def next_question(self):
        #        print(question_number)
        question = self.question_list[self.question_number]
        answer = input(
            f"Q.{self.question_number+1}: {question.text} 'True/False' : ")

        return answer

    def test_answer(self, answer):
        #        print(answer)
        if answer.lower() == "true" or answer.lower() == "false":
            self.question_number += 1
            return True
        else:
            print("Please enter 'True' or 'False'")
            return False

    def score(self, answer):
        the_real_answer = self.question_list[self.question_number-1].answer.lower()
        if answer == the_real_answer:
            self.the_score += 1
            print("You got it right ! ")
            print(f"The correct answer was : {answer} ")
            print(
                f"Your current score is: {self.the_score}/{self.question_number}\n")
        else:
            print("That's wrong ! ")
            print(f"The correct answer was : {the_real_answer} ")
            print(
                f"Your current score is: {self.the_score}/{self.question_number}\n")

    def still_has_question(self):
        if self.question_number <= len(self.question_list)-1:
            return True
        else:
            print("You've completed the quiz")
            print(
                f"Your final score was : {self.the_score}/{self.question_number}")

            return False

    def logo_print(self):
        if self.the_score < self.question_number:
            print(moquing)
        else:
            print(gj_bro)
