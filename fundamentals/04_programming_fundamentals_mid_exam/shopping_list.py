shopping_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        print(', '.join(shopping_list))
        break

    command = command.split(" ")
    action = command[0]
    item = command[1]

    if action == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif action == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)
    elif action == "Correct":
        corrected_item = command[2]
        if item in shopping_list:
            for index in range(len(shopping_list)):
                if shopping_list[index] == item:
                    shopping_list[index] = corrected_item
    elif action == "Rearrange":
        # corrected_item = command[2]
        if item in shopping_list:
            arranged_item = shopping_list.remove(item)
            shopping_list.append(item)