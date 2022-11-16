initial_health = 100
initial_bitcoins = 0

dungeons = input().split("|")

for index, current_dungeon in enumerate(dungeons):
    action, amount = current_dungeon.split(' ')
    amount = int(amount)
    # print(action, amount)
    if action == "potion":
        if initial_health + amount > 100:
            healed = 100 - initial_health
            initial_health = 100
        else:
            healed = amount
            initial_health += amount
        print(f"You healed for {healed} hp.")
        print(f"Current health: {initial_health} hp.")
    elif action == "chest":
        initial_bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        initial_health -= amount
        if initial_health > 0:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {index + 1}")
            break

if initial_health > 0:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")