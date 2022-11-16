import re
from os import linesep

text_file = './input.txt'
words_file = './words.txt'
output_file = './output.txt'

search_words = {}
with open(words_file, 'r') as file:
    words = file.readline().strip().split(' ')
    search_words = {word.lower(): 0 for word in words}

with open(text_file, 'r') as file:
    pattern = r'[a-zA-Z\']+'
    for line in file:
        all_line_words = re.findall(pattern, line)
        for word in all_line_words:
            word_lower = word.lower()
            if word_lower in search_words.keys():
                search_words[word_lower] += 1

sorted_dict = dict(sorted(search_words.items(), key=lambda x: -x[1]))
with open(output_file, 'w+') as file:
    for key, value in sorted_dict.items():
        file.write(f'{key} - {value}\n')

with open(output_file, 'r') as file:
    print(file.read())
