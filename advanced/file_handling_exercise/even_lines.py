file_path = 'files/text.txt'
symbols = ["-", ",", ".", "!", "?"]
text = ''

with open(file_path, 'r') as file:
    text = file.readlines()
    print(text)

for row in range(0, len(text), 2):
    for symbol in symbols:
        text[row] = text[row].replace(symbol, '@')

    print(*text[row].split()[::-1], sep=' ')

