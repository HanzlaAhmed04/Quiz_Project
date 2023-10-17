from data import question_data
from question_model import Question
#
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
#
# print(question_bank[0].text)
# print(question_bank[0].answer)





























#class User:
 #   pass

# class User:
#
#     def __init__(self, name, age):
#
#         self.name = name
#         self.age = age
#
#
# user_1 = User("Hanzla", 26)
# print(user_1.name)
# print(user_1.age)
# user_2 = User("Ajar", 16)
# print(user_2.name)
# print(user_2.age)
# user_3 = User("Ismail", 27)
# print(user_3.name)
# print(user_3.age)
# user_4 = User("Hamza", 23)
# print(user_4.name)
# print(user_4.age)

# class UserProfile:
#     def __init__(self, user_name, user_id, user_followers, user_following):
#         self.user_name = user_name
#         self.user_id = user_id
#         self.user_followers = user_followers
#         self.user_following = user_following
#
# user_1 = UserProfile("Hanzla", 123, 50000, 500)
# print(f"Name is {user_1.user_name}, ID is {user_1.user_id}, Followers: {user_1.user_followers}, Following: {user_1.user_following}")
# user_2 = UserProfile("Ajar", 1234, 40000, 400)
# print(f"Name is {user_2.user_name}, ID is {user_2.user_id}, Followers: {user_2.user_followers}, Following: {user_2.user_following}")
# user_3 = UserProfile("Ismail", 1235, 30000, 300)
# print(f"Name is {user_3.user_name}, ID is {user_3.user_id}, Followers: {user_3.user_followers}, Following: {user_3.user_following}")
# user_4 = UserProfile("Hamza", 1236, 20000, 200)
# print(f"Name is {user_4.user_name}, ID is {user_4.user_id}, Followers: {user_4.user_followers}, Following: {user_4.user_following}")

# class Car():
#     def __init__(self, seats):
#         self.seats = seats
#
#     def enter_race_mode(self):
#         self.seats = 2
#
# my_car = Car(5)
# print(my_car.seats)
# my_car.enter_race_mode()
# print(my_car.seats)