def initial_cars():
    cars_dict = {}
    number_of_cars = int(input())
    for _ in range(number_of_cars):
        car, mileage, fuel = input().split('|')
        cars_dict[car] = {'mileage': int(mileage), 'fuel': int(fuel)}
    return cars_dict


def drive(cars_dict, car, distance, fuel):
    if cars_dict[car]['fuel'] < fuel:
        print(f"Not enough fuel to make that ride")
    else:
        cars_dict[car]['mileage'] += distance
        cars_dict[car]['fuel'] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if cars_dict[car]['mileage'] >= 100_000:
        del cars_dict[car]
        print(f"Time to sell the {car}!")
    return cars_dict


def refuel(cars_dict, car, fuel):
    fuel_added = 0
    if cars_dict[car]['fuel'] + fuel > 75:
        fuel_added = 75 - cars_dict[car]['fuel']
        cars_dict[car]['fuel'] = 75
    else:
        fuel_added = fuel
        cars_dict[car]['fuel'] += fuel
    print(f"{car} refueled with {fuel_added} liters")
    return cars_dict


def revert(cars_dict, car, kilometers):
    if cars_dict[car]['mileage'] - kilometers < 10_000:
        cars_dict[car]['mileage'] = 10_000
    else:
        cars_dict[car]['mileage'] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return cars_dict


def print_cars_status(cars_dict):
    for car in cars_dict.keys():
        print(f"{car} -> Mileage: {cars_dict[car]['mileage']} kms, Fuel in the tank: {cars_dict[car]['fuel']} lt.")



def need_for_speed():
    cars_dict = initial_cars()

    while True:
        command = input().split(' : ')
        if command[0] == 'Stop':
            print_cars_status(cars_dict)
            break

        action = command[0]
        if action == 'Drive':
            car, distance, fuel = command[1], int(command[2]), int(command[3])
            cars_dict = drive(cars_dict, car, distance, fuel)
        elif action == 'Refuel':
            car, fuel = command[1], int(command[2])
            cars_dict = refuel(cars_dict, car, fuel)
            pass
        elif action == 'Revert':
            car, kilometers = command[1], int(command[2])
            cars_dict = revert(cars_dict, car, kilometers)


need_for_speed()