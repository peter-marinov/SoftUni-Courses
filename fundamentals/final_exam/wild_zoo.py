def add(animals_dict, areas_with_hungry_animals, animal_name, needed_food_quantity, area):
    if animal_name not in animals_dict.keys():
        animals_dict[animal_name] = {}
        animals_dict[animal_name] = {'area': ''}
        animals_dict[animal_name] = {'food': 0}
    animals_dict[animal_name]['area'] = area
    animals_dict[animal_name]['food'] += needed_food_quantity
    if area not in areas_with_hungry_animals.keys():
        areas_with_hungry_animals[area] = []
    if animal_name not in areas_with_hungry_animals[area]:
        areas_with_hungry_animals[area].append(animal_name)
    return animals_dict, areas_with_hungry_animals


def feed(animals_dict, areas_with_hungry_animals, animal_name, food):
    if animal_name in animals_dict.keys():
        animals_dict[animal_name]['food'] -= food
        if animals_dict[animal_name]['food'] <= 0:
            area = animals_dict[animal_name]['area']
            del animals_dict[animal_name]
            areas_with_hungry_animals[area].remove(animal_name)
            print(f'{animal_name} was successfully fed')

    return animals_dict, areas_with_hungry_animals


animals_dict = {}
areas_with_hungry_animals = {}

while True:
    command = input().split(":")
    if command[0] == 'EndDay':
        print('Animals:')
        for animal in animals_dict.keys():
            print(f"{animal} -> {animals_dict[animal]['food']}g")

        print("Areas with hungry animals:")
        for area in areas_with_hungry_animals.keys():
            if areas_with_hungry_animals[area]:
                print(f"{area}: {len(areas_with_hungry_animals[area])}")
        break

    action = command[0]
    no_strip_command = command[1].strip()
    no_strip_command = no_strip_command.split('-')
    if action == 'Add':
        animal_name, needed_food_quantity, area = no_strip_command[0], int(no_strip_command[1]), no_strip_command[2]
        animals_dict, areas_with_hungry_animals = add(animals_dict, areas_with_hungry_animals, animal_name, needed_food_quantity, area)
    elif action == 'Feed':
        animal_name, food = no_strip_command[0], int(no_strip_command[1])
        animals_dict, areas_with_hungry_animals = feed(animals_dict, areas_with_hungry_animals, animal_name, food)