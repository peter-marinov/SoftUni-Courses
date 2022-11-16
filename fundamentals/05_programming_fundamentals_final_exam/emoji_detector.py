import re

emoji_pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
numbers_pattern = r'\d'

emoji_list = []

string = input()

cool_threshold = 1
digits = re.findall(numbers_pattern, string)
for digit in digits:
    cool_threshold *= int(digit)

matches = re.findall(emoji_pattern, string)
for match in matches:
    emoji_threshold = 0
    for symbol in match[1]:
        emoji_threshold += ord(symbol)
    if emoji_threshold > cool_threshold:
        emoji_list.append(f'{match[0]}{match[1]}{match[0]}')


print(f'Cool threshold: {cool_threshold}')
if len(matches) > 0:
    print(f'{len(matches)} emojis found in the text. The cool ones are:')
    for emoji in emoji_list:
        print(''.join(emoji))
