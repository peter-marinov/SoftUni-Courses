def drive(cars_dict, car, distance, fuel):
    if cars_dict[car][1] < fuel:
        print("Not enough fuel to make that ride")
    else:
        cars_dict[car][0] += distance
        cars_dict[car][1] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if cars_dict[car][0] >= 100_000:
        del cars_dict[car]
        print(f"Time to sell the {car}!")
    return cars_dict


def refuel(cars_dict, car, fuel):
    if cars_dict[car][1] + fuel > 75:
        added_fuel = 75 - cars_dict[car][1]
        cars_dict[car][1] = 75
    else:
        cars_dict[car][1] += fuel
        added_fuel = fuel

    print(f"{car} refueled with {added_fuel} liters")
    return cars_dict


def revert(cars_dict, car, kilometers):
    if cars_dict[car][0] - kilometers < 10_000:
        cars_dict[car][0] = 10_000
    else:
        cars_dict[car][0] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return cars_dict



number_of_cars = int(input())

cars_dict = {}
for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars_dict[car] = [int(mileage), int(fuel)]

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break

    action = command[0]
    if action == "Drive":
        cars_dict = drive(cars_dict, command[1], int(command[2]), int(command[3]))
    elif action == "Refuel":
        cars_dict = refuel(cars_dict, command[1], int(command[2]))
    elif action == "Revert":
        cars_dict = revert(cars_dict, command[1], int(command[2]))

for car in cars_dict.keys():
    print(f"{car} -> Mileage: {cars_dict[car][0]} kms, Fuel in the tank: {cars_dict[car][1]} lt.")