password = input()

while True:
    command = input().split()

    if command[0] == "Done":
        break

    action = command[0]
    if action == "TakeOdd":
        odd_string = ''
        for index in range(len(password)):
            if index % 2 != 0:
                odd_string += password[index]
        password = odd_string
        print(password)
    elif action == "Cut":
        index, length = int(command[1]), int(command[2])
        end_index = index + length
        password = password.replace(password[index: end_index], '', 1)
        print(password)
    elif action == "Substitute":
        substring, substitute = command[1:]
        if substring not in password:
            print("Nothing to replace!")
        else:
            password = password.replace(substring, substitute)
            print(password)

print(f"Your password is: {password}")