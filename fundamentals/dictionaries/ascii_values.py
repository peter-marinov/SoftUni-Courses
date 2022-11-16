ascii_dict = {}

letters = input().split(', ')
ascii_dict = {letter: ord(str(letter)) for letter in letters}
print(ascii_dict)

