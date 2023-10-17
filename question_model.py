class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def abc(self):
        # print(self.text)
        self.text = 2
        # return self.text

question_1 = Question("Karachi is the capital of Pakistan", True)
question_2 = Question("Florida is the capital of USA", False)

print(question_2.abc())

#
# print(question_1.text)
# print(question_1.answer)