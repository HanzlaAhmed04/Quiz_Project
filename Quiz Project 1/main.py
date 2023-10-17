from data import question_data   # we have data
from question_model import Question   # we have blueprint/class
from quiz_brain import QuizBrain



question_bank = []

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
has_questions = True
while has_questions:
    quiz.next_question()
    if quiz.still_has_question() == False:
        has_questions = False




































































































"""
# Whenever you will define a class's name you will follow pascal case
# Pascal Case: First character of each word in a class name is capitalized
# Camel Case: Every first character of each word is capitalized except first word
# Snake Case: you don't capitalize any word. You connect multiple words using underscore(_)


# Camel Case Examples
# firstName
# lastName
# motherName
# fatherName
#Pascal Case Examples
#UncleName

# Snake case:
#
# first_name
# last_name
# mother_name
# father_name
# uncle_name

# In python you use Pascal Case to name classes
# In python you use snake case for variable names and function/method names



# class User:
#     pass
# user_1 = User()
# user_1.name = "Hanzla"
# user_1.age = 26
# print(user_1.name)
# print(user_1.age)
#
# user_2 = User()
# user_2.name = "ajar"
# user_2.age = 16
# print(user_2.name)
# print(user_2.age)


class User:
    # Define constructor
    # Whenever you create an object from a class
    # Constructor is called by python automatically
    # Constructor is basically a method
    # it is part of the class
    # First parameter of every method inside a class in python is self(keyword)
    def __init__(self):
        print("Constructor called")
        self.name = ''   # We are initializing
        self.age = 0

user_1 = User()
user_2 = User()
user_3 = User()
user_4 = User()


# Create object using values to assign it
class User:
    # Define constrcutor
    # Whenever you create an object from a class
    # Constructor is called by python automatically
    # Constructor is basically a method
    # it is part of the class
    # First parameter of every method inside a class in python is self(keyword)
    def __init__(self, name, age):
        print("Constructor called")
        self.name = name   # We are initializing
        self.age = age

user_1 = User("Hanzla" , 26)
print(user_1.name)
print(user_1.age)
user_2 = User("Ismail", 27)
print(user_2.name)
print(user_2.age)
user_3 = User("Ajar", 16)
print(user_3.name)
print(user_3.age)
user_4 = User("Neha", 50)
print(user_4.name)
print(user_4.age)

# User profile example
class UserProfile:

    def __init__(self, user_name, user_id, user_followers, user_following):
        self.user_name = user_name
        self.user_id = user_id
        self.user_followers = user_followers
        self.user_following = user_following


# ajar , 1 , 50, 60

ajar_profile = UserProfile("ajar", 1, 50, 60)
print(f" name is {ajar_profile.user_name}, id is {ajar_profile.user_id}")


class UserProfile:

    def __init__(self, user_name, user_id, user_followers, user_following):
        self.user_name = user_name
        self.user_id = user_id
        self.user_followers = user_followers
        self.user_following = user_following

    def follow(self, user):
        self.user_followers += 1
        user.user_following += 1


# ajar , 1 , 50, 60

ajar_profile = UserProfile("ajar", 1, 50, 60)
hanzla_profile = UserProfile("Hanzla", 2, 50, 60)
hanzla_profile.follow(ajar_profile)

print(ajar_profile.user_following)
print(hanzla_profile.user_followers)


# print(f" name is {ajar_profile.user_name}, id is {ajar_profile.user_id}")


class Car:
    def __init__(self, seats):
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 2


my_car = Car(5)
print(my_car.seats)
my_car.enter_race_mode()
print(my_car.seats)

# whenever a function is part of an object it is called method
# if a functuoin is not part of a object/class it is called function


# def add():
#
# functionality:
#     post
#     share
#     like
#     comment
#     change picture
# attributes:
#     first name
#     last name
#     age
#     email
#     password
#     mobile number
#
#
# attributes:
#     addresss
#     order_info
#     phone number
#     name
# functionlaity:
#     order
#     cancel_order
#     contact_rider


"""
