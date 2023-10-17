class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_question(self):
   #     print(self.question_number)
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False)   ")
        if current_question.answer.lower() == user_answer.lower():
            self.score += 1
        print(f"your score is {self.score}/{self.question_number}")





#A slug's blood is green(True/False)
