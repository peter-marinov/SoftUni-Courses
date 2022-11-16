def insert_space(secret_message, index):
    if 0 <= index < len(secret_message):
        secret_message = secret_message[:index] + ' ' + secret_message[index:]
    print(secret_message)
    return secret_message


def reverse(secret_message, substring):
    if substring in secret_message:
        secret_message = secret_message.replace(substring, '', 1) + substring[::-1]
        print(secret_message)
    else:
        print("error")
    return secret_message


def change_all(secret_message, substring, replacement):
    secret_message = secret_message.replace(substring, replacement)
    print(secret_message)
    return secret_message

secret_message = input()

while True:
    command = input().split(":|:")
    action = command[0]
    if action == "Reveal":
        break
    elif action == "InsertSpace":
        secret_message = insert_space(secret_message, int(command[1]))
    elif action == "Reverse":
        secret_message = reverse(secret_message, command[1])
    elif action == "ChangeAll":
        secret_message = change_all(secret_message, command[1], command[2])


print(f"You have a new text message: {secret_message}")


