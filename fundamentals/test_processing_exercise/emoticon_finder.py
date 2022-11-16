text = input()

emoji_list = []
for index in range(len(text)):
    if text[index] == ":":
        current_emoji = text[index:index + 2]
        emoji_list.append(current_emoji)

[print(f"{emoji}") for emoji in emoji_list]