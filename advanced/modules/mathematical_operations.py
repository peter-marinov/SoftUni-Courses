from modules.utils import calculate_expression

first_number, operation, second_number = input().split(' ')

print(calculate_expression(float(first_number), float(second_number), operation))
