travel_stops = input()

while True:
    command = input().split(':')
    if command[0] == 'Travel':
        print(f"Ready for world tour! Planned stops: {travel_stops}")
        break
    action = command[0]
    if action == 'Add Stop':
        index, string = int(command[1]), command[2]
        if 0 <= index < len(travel_stops):
            travel_stops = travel_stops[:index] + string + travel_stops[index:]
            # print(travel_stops)
    elif action == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        if  0 <= start_index < len(travel_stops) and  0 <= end_index < len(travel_stops):
            travel_stops = travel_stops[:start_index] + travel_stops[end_index + 1:]
            # print(travel_stops)
    elif action == 'Switch':
        old_string, new_string = command[1:]
        if old_string in travel_stops:
            travel_stops = travel_stops.replace(old_string, new_string)
    print(travel_stops)

