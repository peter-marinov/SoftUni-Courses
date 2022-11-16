parking_space_dict = {}

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    action, car_owner_name = command[0], command[1]
    if action == "register":
        car_id = command[2]
        if car_owner_name in parking_space_dict.keys():
            print(f"ERROR: already registered with plate number {parking_space_dict[car_owner_name]}")
        else:
            parking_space_dict[car_owner_name] = car_id
            print(f"{car_owner_name} registered {parking_space_dict[car_owner_name]} successfully")
    elif action == "unregister":
        if car_owner_name not in parking_space_dict.keys():
            print(f"ERROR: user {car_owner_name} not found")
        else:
            del parking_space_dict[car_owner_name]
            print(f"{car_owner_name} unregistered successfully")

for user in parking_space_dict.keys():
    print(f"{user} => {parking_space_dict[user]}")