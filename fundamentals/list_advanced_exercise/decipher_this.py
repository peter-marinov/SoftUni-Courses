messages = input().split()
final_message = []
for message in messages:
    number = ""
    current_message = ""
    for symbol in message:
        if symbol.isdigit():
            number += symbol
        else:
            break
    message = message.replace(number, '')
    number = int(number)
    current_message += chr(number)
    if len(message) >= 2:
        message = message[-1] + message[1:-1] + message[0]
    # message[0], message[-1] = message[-1], message[0]
    # print(message)
    current_message += message
    final_message.append(current_message)

print(" ".join(final_message))