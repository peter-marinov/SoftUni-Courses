pirate_ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
max_health_capacity = int(input())


is_sunken = False
while True:
    command = input()
    if command == "Retire":
        print(f"Pirate ship status: {sum(pirate_ship_status)}")
        print(f"Warship status: {sum(warship_status)}")
        break

    command = command.split(' ')
    action = command[0]

    if action == "Fire":
        index, damage = int(command[1]), int(command[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break
    elif action == "Defend":
        start_index, end_index, damage =  int(command[1]), int(command[2]), int(command[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            if start_index < end_index:
                for pirate_ship_index in range(start_index, end_index + 1):
                    pirate_ship_status[pirate_ship_index] -= damage
                    if pirate_ship_status[pirate_ship_index] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        is_sunken = True
                        break
            elif start_index > end_index:
                for pirate_ship_index in range(end_index, start_index + 1):
                    pirate_ship_status[pirate_ship_index] -= damage
                    if pirate_ship_status[pirate_ship_index] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        is_sunken = True
                        break
            else:
                pirate_ship_status[start_index] -= damage
                if pirate_ship_status[start_index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_sunken = True
                    break
        if is_sunken:
            break
    elif action == "Repair":
        index, health = int(command[1]), int(command[2])
        if 0 <= index < len(pirate_ship_status):
            if pirate_ship_status[index] + health > max_health_capacity:
                pirate_ship_status[index] = max_health_capacity
            else:
                pirate_ship_status[index] += health
    elif action == "Status":
        status_list = []
        status_list = [num for num in pirate_ship_status if num < max_health_capacity * 0.2]
        print(f"{len(status_list)} sections need repair.")

    # print(pirate_ship_status)
    # print(warship_status)