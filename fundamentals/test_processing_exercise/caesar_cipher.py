text = input()

encrypted_text = ''

for symbol in text:
    ascii_number = ord(symbol) + 3
    encrypted_text += chr(ascii_number)

print(encrypted_text)