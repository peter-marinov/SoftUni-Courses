def rate(plants_dict, dict_items):
    plant, rating = dict_items.split('-')
    plant = plant.strip()
    rating = float(rating.strip())
    if plant in plants_dict.keys():
        plants_dict[plant][-1].append(rating)
    else:
        print("error")

    return plants_dict


def update(plants_dict, dict_items):
    plant, new_rarity = dict_items.split('-')
    plant = plant.strip()
    new_rarity = int(new_rarity.strip())
    if plant in plants_dict.keys():
        plants_dict[plant][0] = new_rarity
    else:
        print("error")

    return plants_dict


def reset(plants_dict, dict_items):
    plant = dict_items.strip()
    if plant in plants_dict.keys():
        plants_dict[plant][-1] = []
    else:
        print("error")

    return plants_dict


number_of_lines = int(input())

plants_dict = {}

for _ in range(number_of_lines):
    plant, rarity = input().split('<->')
    rarity = int(rarity)
    if plant not in plants_dict.keys():
        plants_dict[plant] = []
    plants_dict[plant] = [rarity, []]

while True:
    command = input().split(":")

    if command[0] == "Exhibition":
        break

    action, dict_items = command
    if action == "Rate":
        plants_dict = rate(plants_dict, dict_items)
    elif action == "Update":
        plants_dict = update(plants_dict, dict_items)
    elif action == "Reset":
        plants_dict = reset(plants_dict, dict_items)

print("Plants for the exhibition:")
for key in plants_dict.keys():
    average_rating = 0
    if len(plants_dict[key][-1]) > 0:
        average_rating = sum(plants_dict[key][-1]) / len(plants_dict[key][-1])
    print(f"- {key}; Rarity: {plants_dict[key][0]}; Rating: {average_rating:.2f}")


