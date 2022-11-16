# a = 5
# b = 10
#
# if b > a:
#     print(b)
#     b = 100
#     print(b)
#
# print(b)

import random

#####
# number = random.randint(1, 3)
#
# guess_number = int(input('Enter the number between 1 and 3: '))
#
# if guess_number == number:
#     print('successful choice')
# print(number)
#####

#####
# ascii_value = random.randint(65, 90)
# letter = chr(ascii_value)
# print(letter)
#####

#####
questions = ['Monday', 'Tuesday', 'weekdays', 'Thursday', 'Friday']
for _ in range (10):
    current_questions = random.choice(questions)
    print(current_questions)
# random_day = random.choice(weekdays)

#####