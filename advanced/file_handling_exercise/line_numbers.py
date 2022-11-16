from string import punctuation

input_file_path = 'files/text.txt'
output_file_path = 'files/output.txt'

output_file = open(output_file_path, 'w')

with open(input_file_path, 'r') as text_file:
    text = text_file.readlines()

for index in range(len(text)):
    row = text[index]

    letters = 0
    marks = 0
    for symbol in row:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {index+1}: {''.join(row[:-1])} ({letters})({marks})\n")

output_file.close()