def add_cars(cars, number):
    for _ in range(number):
        car_type, mileage, fuel_quantity = input().split('|')
        cars[car_type] = {'mileage': int(mileage), 'fuel_quantity': int(fuel_quantity)}
    return cars


def cars_usage(cars):
    while True:
        full_command = input().split(' : ')

        if full_command[0] == 'Stop':
            break

        command = full_command[0]
        car = full_command[1]

        if command == 'Drive':
            distance = int(full_command[2])
            fuel = int(full_command[3])
            if cars[car]['fuel_quantity'] < fuel:
                print("Not enough fuel to make that ride")
            else:
                cars[car]['mileage'] += distance
                cars[car]['fuel_quantity'] -= fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]['mileage'] >= 100000:
                del cars[car]
                print(f"Time to sell the {car}!")

        elif command == 'Refuel':
            fuel = int(full_command[2])
            if cars[car]['fuel_quantity'] + fuel > 75:
                fuel_refilled = 75 - cars[car]['fuel_quantity']
            else:
                fuel_refilled = fuel
            cars[car]['fuel_quantity'] += fuel_refilled
            print(f"{car} refueled with {fuel_refilled} liters")

        elif command == 'Revert':
            km = int(full_command[2])
            new_km = cars[car]['mileage'] - km
            if new_km < 10000:
                cars[car]['mileage'] = 10000
            else:
                cars[car]['mileage'] = new_km
                print(f"{car} mileage decreased by {km} kilometers")

    return cars


def print_function(cars):
    for c in cars:
        print(f"{c} -> Mileage: {cars[c]['mileage']} kms, Fuel in the tank: {cars[c]['fuel_quantity']} lt.")


def cars_discovery(number):
    cars = {}
    add_cars(cars, number)
    cars_usage(cars)
    print_function(cars)


num = int(input())
cars_discovery(num)