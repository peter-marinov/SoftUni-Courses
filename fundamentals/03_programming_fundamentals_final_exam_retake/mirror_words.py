import re

text = input()

search_pattern = r'([@#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'
filtered_data = []
match_count = 0
for match in re.finditer(search_pattern, text):
    match_count += 1
    if match.group(2) == match.group(3)[::-1]:
        filtered_data.append(f'{match.group(2)} <=> {match.group(3)}')

if match_count > 0:
    print(f'{match_count} word pairs found!')
else:
    print('No word pairs found!')
if len(filtered_data) == 0:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(filtered_data))
