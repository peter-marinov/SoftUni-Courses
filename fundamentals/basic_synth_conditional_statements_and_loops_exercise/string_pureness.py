number_of_strings = int(input())

for string in range(number_of_strings):
    current_word = input()
    if ',' in current_word or '.' in current_word or '_' in current_word:
        print(f"{current_word} is not pure!")
    else:
        print(f"{current_word} is pure.")