def decrypt_func(encrypted_message, command):
    action = command[0]
    if action == "Move":
        number_of_letters = int(command[1])
        letters_to_move = encrypted_message[:number_of_letters]
        encrypted_message = encrypted_message[number_of_letters :]
        encrypted_message += letters_to_move
        # print(encrypted_message)
        return encrypted_message
    elif action == "Insert":
        index, value = int(command[1]), command[2]
        first_str_half = encrypted_message[:index]
        second_str_half = encrypted_message[index:]
        encrypted_message = first_str_half + value + second_str_half
        # print(encrypted_message)
        return encrypted_message
    elif action == "ChangeAll":
        substring, replacement = command[1], command[2]
        while substring in encrypted_message:
            # print(encrypted_message)
            encrypted_message = encrypted_message.replace(substring, replacement)
            # print(encrypted_message)
        return encrypted_message

encrypted_message = input()

while True:
    command = input().split('|')
    if command[0] == "Decode":
        break
    encrypted_message = decrypt_func(encrypted_message, command)
print(f"The decrypted message is: {encrypted_message}")


