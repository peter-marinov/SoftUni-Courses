'''
from math import floor

text = list(input().split())

result = 0
result_is_changed = False
current_list = list(text)
for symbol in text:
    index = current_list.index(symbol)
    if symbol in ['*', '+', '-', '/'] and index != 0:
        for current_index in range(0, index):
            if symbol == '*':
                if not result_is_changed:
                    result += int(current_list[0])
                else:
                    result *= int(current_list[current_index])
            elif symbol == '+':
                result += int(current_list[current_index])
            elif symbol == '-':
                if not result_is_changed:
                    result += int(current_list[0])
                else:
                    result -= int(current_list[current_index])
            elif symbol == '/':
                if not result_is_changed:
                    result /= int(current_list[0])
                else:
                    result /= int(current_list[current_index])

            result_is_changed = True

        result = floor(result)
        current_list = current_list[index + 1:]


print(result)
'''

# Reduce loops all values from a list and can do math operation and it will return the final value in the list

from functools import reduce

expression = input().split()
stack = []

for item in expression:
    if item.lstrip('-').isnumeric():
        stack.append(int(item))
    else:
        if item == '*':
            stack = [reduce(lambda x, y: x * y, stack)]
        elif item == '/':
            stack = [reduce(lambda x, y: x // y, stack)]
        elif item == '+':
            stack = [reduce(lambda x, y: x + y, stack)]
        elif item == '-':
            stack = [reduce(lambda x, y: x - y, stack)]

print(stack[0])
