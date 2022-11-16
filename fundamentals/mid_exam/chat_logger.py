chat_history = []

while True:
    command = input()
    if command == "end":
        print('\n'.join(chat_history))
        break

    command = command.split(' ')
    action = command[0]

    if action == "Chat":
        chat_msg = command[1]
        chat_history.append(chat_msg)
    elif action == "Delete":
        delete_msg = command[1]
        if delete_msg in chat_history:
            chat_history.remove(delete_msg)
    elif action == "Edit":
        msg_to_edit = command[1]
        edited_msg = command[2]
        if msg_to_edit in chat_history:
            chat_history[chat_history.index(msg_to_edit)] = edited_msg
    elif action == "Pin":
        pin_msg = command[1]
        if pin_msg in chat_history:
            chat_history.remove(pin_msg)
            chat_history.append(pin_msg)
    elif action == "Spam":
        spam_msgs = command[1:]
        chat_history = chat_history + spam_msgs
