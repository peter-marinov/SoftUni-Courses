def add_stop(string, command):
    index, value = int(command[1]), command[2]
    if 0 <= index <= len(string):
        string = string[:index] + value + string[index:]

    return string


def remove_stop(string, command):
    start_index, end_index = int(command[1]), int(command[2])
    if 0 <= start_index < len(string) and 0 <= end_index < len(string):
        string = string.replace(string[start_index:end_index + 1], "")

    return string


def switch_stop(string, command):
    old_string, new_string = command[1], command[2]
    string = string.replace(old_string, new_string)

    return string


world_tour_string = input()

while True:
    command = input().split(':')
    if command[0] == 'Travel':
        break

    action = command[0]

    if action == 'Add Stop':
        world_tour_string = add_stop(world_tour_string, command)
    elif action == 'Remove Stop':
        world_tour_string = remove_stop(world_tour_string, command)
    elif action == 'Switch':
        world_tour_string = switch_stop(world_tour_string, command)

    print(world_tour_string)

print(f"Ready for world tour! Planned stops: {world_tour_string}")
