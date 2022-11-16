import re

text = input()

pattern = r'([@#])([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1'

result = re.findall(pattern, text)
mirror_words_list = []
if result:
    print(f"{len(result)} word pairs found!")
    for word in result:
        if word[1] == word[2][::-1]:
            mirror_words_list.append(f'{word[1]} <=> {word[2]}')
    if len(mirror_words_list) > 0:
        print("The mirror words are:")
        print(', '.join(mirror_words_list))
    else:
        print('No mirror words!')


else:
    print("No word pairs found!")
    print('No mirror words!')
