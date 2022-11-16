from collections import deque

firework_effects = deque(map(int, input().split(', ')))
explosives_power = list(map(int, input().split(', ')))

fireworks_dict = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

party = False

while firework_effects and explosives_power:
    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue

    if explosives_power[-1] <= 0:
        explosives_power.pop()
        continue

    current_sum = firework_effects[0] + explosives_power[-1]
    if current_sum % 3 == 0 and not current_sum % 5 == 0:
        fireworks_dict["Palm Fireworks"] += 1
        firework_effects.popleft()
        explosives_power.pop()
    elif current_sum % 5 == 0 and not current_sum % 3 == 0:
        fireworks_dict["Willow Fireworks"] += 1
        firework_effects.popleft()
        explosives_power.pop()
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks_dict["Crossette Fireworks"] += 1
        firework_effects.popleft()
        explosives_power.pop()
    else:
        firework_effects.append(firework_effects.popleft() - 1)

    if fireworks_dict["Palm Fireworks"] >= 3 and fireworks_dict["Willow Fireworks"] >= 3 and \
            fireworks_dict["Crossette Fireworks"] >= 3:
        party = True
        break

if party:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")

if explosives_power:
    print(f"Explosive Power left: {', '.join(map(str, explosives_power))}")

for key, value in fireworks_dict.items():
    print(f'{key}: {value}')
