def plunder(cities_dict, town, people, gold):
    if town in cities_dict.keys():
        cities_dict[town][0] -= people
        cities_dict[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if cities_dict[town][0] == 0 or cities_dict[town][1] == 0:
            del cities_dict[town]
            print(f'{town} has been wiped off the map!')
    return cities_dict


def prosper(cities_dict, town, gold):
    if gold < 0:
        print('Gold added cannot be a negative number!')
    else:
        cities_dict[town][1] += gold
        print(f'{gold} gold added to the city treasury. {town} now has {cities_dict[town][1]} gold.')
    return cities_dict


cities_dict = {}

while True:
    command = input().split('||')
    if command[0] == 'Sail':
        break
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities_dict.keys():
        cities_dict[city] = [0, 0]
    cities_dict[city][0] += population
    cities_dict[city][1] += gold

while True:
    command = input().split('=>')
    if command[0] =='End':
        break

    action = command[0]
    if action == 'Plunder':
        cities_dict = plunder(cities_dict, command[1], int(command[2]), int(command[3]))
    elif action == 'Prosper':
        cities_dict = prosper(cities_dict, command[1], int(command[2]))

if len(cities_dict.keys()) == 0:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    print(f'Ahoy, Captain! There are {len(cities_dict.keys())} wealthy settlements to go to:')
    for town in cities_dict.keys():
        print(f'{town} -> Population: {cities_dict[town][0]} citizens, Gold: {cities_dict[town][1]} kg')

