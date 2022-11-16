# def even_or_odd_number(num):
#     if num % 2 == 0:
#         return "Even number"
#     else:
#         return "Odd number"
# number = int(input())
# print(even_or_odd_number(number))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
#
# result = list (filter(lambda x: x % 2 == 0, numbers))
#
# print(result)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
#
#
# def check_numbers(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# result = list(filter(check_numbers, numbers))
# print(result)

# numbers = list(map(int, input().split(', ')))
# print(numbers)

# numbers = [2, 3, 6, 8, 10]
#
# def square_number(number):
#     return number * number
#
# square_numbers = list(map(square_number, numbers))

# def print_header():
#     print('This is header!')
#
# print_header()
# def sum_function(a, b):
#     return a + b
#
#
# def substract_function(a, b):
#     return a - b
#
#
# def operations_with_numbers(a, b):
#     print(sum_function(a, b))
#     print(substract_function(a, b))
#
#
# operations_with_numbers(2, 4)

# def countdown(number):
#     print(number)
#
#     if number == 0:
#         return
#     else:
#         countdown(number - 1)
#
# countdown(5)

# def greet():
#     """This function just says Hello"""
#     return f'Hello!'

# username = input()
# print(greet(username))
# print(greet.__doc__)


add_func = lambda a = 20: lambda b: a + b
a = add_func()
print(add_func(3))