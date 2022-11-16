treasure_chest_loot = input().split('|')

while True:
    command = input()
    if command == "Yohoho!":
        if treasure_chest_loot:
            average_gain = 0
            average_gain = sum([len(loot) for loot in treasure_chest_loot]) / len(treasure_chest_loot)
            print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
        else:
            print("Failed treasure hunt.")
        break

    command = command.split(' ')
    action = command[0]

    if action == "Loot":
        items = [item for item in command[1:] if item not in treasure_chest_loot]
        treasure_chest_loot = items[::-1] + treasure_chest_loot
    elif action == "Drop":
        index = int(command[1])
        if 0 < index <= len(treasure_chest_loot):
            item = treasure_chest_loot[index]
            treasure_chest_loot.pop(index)
            treasure_chest_loot.append(item)
    elif action == "Steal":
        stolen_loots = int(command[1])
        if stolen_loots >= len(treasure_chest_loot):
            print(', '.join(treasure_chest_loot))
            treasure_chest_loot = []
        else:
            print(', '.join(treasure_chest_loot[len(treasure_chest_loot) - stolen_loots:]))
            del treasure_chest_loot[len(treasure_chest_loot) - stolen_loots:]

    # print(treasure_chest_loot)