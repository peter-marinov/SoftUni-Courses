text = input()
strength = 0
new_text = ''
for index in range(len(text)):
    if strength > 0 and text[index] != ">":
        strength -= 1
    elif text[index] == ">":
        strength += int(text[index + 1])
        new_text += text[index]
    else:
        new_text += text[index]

print(new_text)