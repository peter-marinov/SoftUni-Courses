text = input()

final_text = ''
for symbol in text:
    if final_text == '':
        final_text += symbol
    if symbol != final_text[-1]:
        final_text += symbol

print(final_text)