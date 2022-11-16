from string import punctuation

with open("./source/text.txt") as source:
    lines = source.readlines()
    lines = [line.strip() for line in lines]

with open("./source/output.txt", "a") as output:
    for i in range(len(lines)):
        line = lines[i]

        letters = 0
        marks = 0

        for char in line:
            if char in punctuation:
                marks += 1
            elif char.isalpha():
                letters += 1

        output.write(f"Line {i+1}: {line} ({letters}) ({marks})\n")

