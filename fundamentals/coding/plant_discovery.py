number_of_plants = int(input())

plants_dict = {}
for _ in range(number_of_plants):
    plant, rarity = input().split('<->')
    if plant not in plants_dict.keys():
        plants_dict[plant] = {}
        plants_dict[plant]['rating'] = []
    plants_dict[plant]['rarity'] = int(rarity)


while True:
    command = input().split(':')
    action = command[0]
    if action == 'Exhibition':
        break

    command_after_strip = command[1].strip()
    command_after_strip = command_after_strip.split(' - ')
    plant = command_after_strip[0]
    if plant in plants_dict.keys():
        if action == 'Rate':
            rating = int(command_after_strip[1])
            plants_dict[plant]['rating'].append(int(rating))
        elif action == 'Update':
            new_rarity = int(command_after_strip[1])
            plants_dict[plant]['rarity'] = new_rarity
        elif action == 'Reset':
            plants_dict[plant]['rating'] = []
    else:
        print('error')

print('Plants for the exhibition:')
for current_plant in plants_dict.keys():
    average_rating = 0
    if len(plants_dict[current_plant]['rating']) > 0:
        average_rating = sum(plants_dict[current_plant]['rating']) / len(plants_dict[current_plant]['rating'])
    print(f"- {current_plant}; Rarity: {plants_dict[current_plant]['rarity']}; Rating: {average_rating:.2f}")