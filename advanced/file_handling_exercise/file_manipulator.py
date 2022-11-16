import os
target_directory = './files/'

while True:
    command = input().split('-')
    action = command[0]

    if action == 'End':
        break

    if action == 'Create':
        file_name = command[1]
        with open(target_directory + file_name, 'w') as file:
            pass
    elif action == 'Add':
        file_name = command[1]
        content = command[2]
        with open(target_directory + file_name, 'a') as file:
            file.write(content + '\n')

    elif action == 'Replace':
        file_name = command[1]
        old_string = command[2]
        new_string = command[3]
        try:
            # open the file as read and read all the lines
            with open(target_directory + file_name, 'r') as file:
                text = file.readlines()
            # open the file as write ( create a new file ) to write the update lines in the file
            with open(target_directory + file_name, 'w') as file:
                for index in range(len(text)):
                    text[index] = text[index].replace(old_string, new_string)
                    file.write(text[index])
        except FileNotFoundError:
            print("An error occurred")

    elif action == 'Delete':
        file_name = command[1]
        try:
            os.remove(target_directory + file_name)
        except FileNotFoundError:
            print("An error occurred")