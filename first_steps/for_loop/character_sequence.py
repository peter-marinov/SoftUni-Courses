text = input()

text_len = len(text)

for letter in range(0, text_len):
    print(text[letter])

for letter in text:
    print(letter)