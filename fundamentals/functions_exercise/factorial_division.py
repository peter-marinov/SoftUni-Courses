import math


def factorial_calc(number):
    return math.factorial(number)


first_number = int(input())
second_number = int(input())
first_number_factorial = factorial_calc(first_number)
second_number_factorial = factorial_calc(second_number)
print(f'{first_number_factorial/second_number_factorial:.2f}')
