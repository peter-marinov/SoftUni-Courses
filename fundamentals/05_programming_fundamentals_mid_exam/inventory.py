journal = input().split(', ')

while True:
    command = input()
    if command == "Craft!":
        print(', '.join(journal))
        break

    action, item = command.split(' - ')

    if action == "Collect":
        if item not in journal:
            journal.append(item)
    elif action == "Drop":
        if item in journal:
            journal.remove(item)
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in journal:
            index = journal.index(old_item)
            journal.insert(index + 1, new_item)
    elif action == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)
