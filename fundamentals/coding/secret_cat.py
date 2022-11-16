message = input()

while True:
    command = input().split(':|:')
    if command[0] == "Reveal":
        print(f"You have a new text message: {message}")
        break

    action = command[0]
    if action == 'InsertSpace':
        index = int(command[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif action == 'Reverse':
        substring = command[1]
        if substring in message:
            message = message.replace(substring, '', 1) + substring[::-1]
            print(message)
        else:
            print('error')
    elif action == 'ChangeAll':
        substring, replacement = command[1:]
        message = message.replace(substring, replacement)
        print(message)

