'''
def operate(operator, *args):
    if operator == '+':
        total = 0
        for el in args:
            total += el
        return total
    elif operator == '-':
        total = 0
        for el in args:
            total -= el
        return total
    elif operator == '*':
        total = 1
        for el in args:
            total *= el
        return total
    elif operator == '/':
        total = args[0]
        if len(args) > 1:
            for el in args[1:]:
                if total != 0 and el != 0:
                    total /= el
        return total
'''
from functools import reduce


def operate(operator, *numbers):
    result = 0
    if operator == '+':
        result = reduce(lambda x, y: x + y, numbers)
    elif operator == '-':
        result = reduce(lambda x, y: x - y, numbers)
    elif operator == '*':
        result = reduce(lambda x, y: x * y, numbers)
    elif operator == '/':
        result = reduce(lambda x, y: x / y, numbers)
    return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))