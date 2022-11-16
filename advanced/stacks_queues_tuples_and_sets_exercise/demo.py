text = set(input().split())

result = 0
current_list = list(text)
for symbol in text:
    index = current_list.index(symbol)
    if symbol in ['*', '+', '-', '/']:
        for current_index in range(0, index):
            if symbol == '*':
                result *= int(current_list[current_index])
            elif symbol == '+':
                result += int(current_list[current_index])
            elif symbol == '-':
                result -= int(current_list[current_index])
            elif symbol == '/':
                result /= int(current_list[current_index])

        current_list = current_list[index + 1:]

print(result)
