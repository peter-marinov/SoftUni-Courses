def cast_spell(heroes_dict, hero, mana_needed, spell_name):
    if heroes_dict[hero][1] - mana_needed < 0:
        print(f"{hero} does not have enough MP to cast {spell_name}!")
    else:
        heroes_dict[hero][1] -= mana_needed
        print(f"{hero} has successfully cast {spell_name} and now has {heroes_dict[hero][1]} MP!")
    return heroes_dict


def take_damage(heroes_dict, hero, damage, attacker):
    if heroes_dict[hero][0] - damage > 0:
        heroes_dict[hero][0] -= damage
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero][0]} HP left!")
    else:
        del heroes_dict[hero]
        print(f"{hero} has been killed by {attacker}!")

    return heroes_dict


def recharge(heroes_dict, hero, amount):
    if heroes_dict[hero][1] + amount > 200:
        amount_recovered = 200 - heroes_dict[hero][1]
        heroes_dict[hero][1] = 200
    else:
        amount_recovered = amount
        heroes_dict[hero][1] += amount
    print(f"{hero} recharged for {amount_recovered} MP!")
    return heroes_dict


def heal(heroes_dict, hero, amount):
    if heroes_dict[hero][0] + amount > 100:
        amount_recovered = 100 - heroes_dict[hero][0]
        heroes_dict[hero][0] = 100
    else:
        amount_recovered = amount
        heroes_dict[hero][0] += amount
    print(f"{hero} healed for {amount_recovered} HP!")
    return heroes_dict

number_of_heroes = int(input())

heroes_dict = {}
# max_health_points = 100
# max_mana_points = 200
for _ in range(number_of_heroes):
    hero, hp, mp = input().split()
    heroes_dict[hero] = [int(hp), int(mp)]

while True:
    command = input().split(" - ")
    if command[0] == "End":
        break

    action = command[0]
    if action == "CastSpell":
        hero, mana_needed, spell_name = command[1], int(command[2]), command[3]
        heroes_dict = cast_spell(heroes_dict, hero, mana_needed, spell_name)
    elif action == "TakeDamage":
        hero, damage, attacker = command[1], int(command[2]), command[3]
        heroes_dict = take_damage(heroes_dict, hero, damage, attacker)
    elif action == "Recharge":
        hero, amount = command[1], int(command[2])
        heroes_dict = recharge(heroes_dict, hero, amount)
    elif action == "Heal":
        hero, amount = command[1], int(command[2])
        heroes_dict = heal(heroes_dict, hero, amount)

for alive_hero in heroes_dict.keys():
    print(f"{alive_hero}")
    print(f"  HP: {heroes_dict[alive_hero][0]}")
    print(f"  MP: {heroes_dict[alive_hero][1]}")
