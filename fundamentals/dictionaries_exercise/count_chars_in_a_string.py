text = input().split(' ')
char_dict = {}

# for word in text:
#     for letter in word:
#         if letter in char_dict:
#             char_dict[letter] += 1
#         else:
#             char_dict[letter] = 1

for word in text:
    for letter in word:
        if letter not in char_dict.keys():
            char_dict[letter] = 0
        char_dict[letter] += 1

output_print = [f'{letter} -> {count}' for letter, count in char_dict.items()]
print('\n'.join(output_print))