travel_route = input().split("||")
current_fuel = int(input())
current_ammunition = int(input())

for route in range(len(travel_route)):
    if travel_route[route] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    else:
        current_travel_route = travel_route[route].split(' ')
        command, number = current_travel_route[0], int(current_travel_route[1])

        if command == "Travel":
            if current_fuel < number:
                print("Mission failed.")
                break
            else:
                current_fuel -= number
                print(f"The spaceship travelled {number} light-years.")
        elif command == "Enemy":
            if current_ammunition >= number:
                current_ammunition -= number
                print(f"An enemy with {number} armour is defeated.")
            else:
                current_fuel -= number * 2
                if current_fuel < 0:
                    print("Mission failed.")
                    break
                else:
                    print(f"An enemy with {number} armour is outmaneuvered.")
        elif command == "Repair":
            added_fuel = number
            added_ammunition = number * 2
            current_fuel += added_fuel
            current_ammunition += added_ammunition
            print(f"Ammunitions added: {added_ammunition}.")
            print(f"Fuel added: {added_fuel}.")