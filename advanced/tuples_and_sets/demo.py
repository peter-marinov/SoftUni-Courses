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
