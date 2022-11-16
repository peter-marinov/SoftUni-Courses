symbols = ["-", ",", ".", "!", "?"]

with open("./source/text.txt") as text:
    text_lines = text.readlines()
    text_lines = [line.strip() for line in text_lines]

for row in range(0, len(text_lines), 2):
    for symbol in symbols:
        text_lines[row] = text_lines[row].replace(symbol, "@")

    print(*text_lines[row].split()[::-1], sep=" ")

