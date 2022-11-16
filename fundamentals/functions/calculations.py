# def calculation_func(number_a, number_b, operation):
#     if operation == "multiply":
#         return number_a * number_b
#     elif operation == "divide":
#         return int(number_a / number_b)
#     elif operation == "add":
#         return number_a + number_b
#     elif operation == "subtract":
#         return number_a - number_b
#
# type_of_operation = input()
# first_number = int(input())
# second_number = int(input())
#
# print(calculation_func(first_number, second_number, type_of_operation))

import operator


def calculation_func(number_a, number_b, operation):
    operations_dict = {'multiply': operator.mul,
                       'divide': operator.truediv,
                       'add': operator.add,
                       'subtract': operator.sub}
    return int(operations_dict[operation](number_a, number_b))

type_of_operation = input()
first_number = int(input())
second_number = int(input())

print(calculation_func(first_number, second_number, type_of_operation))