from collections import deque

elves_energy = deque(map(int, input().split(' ')))
materials = list(map(int, input().split(' ')))

total_energy = 0
number_of_toys = 0

count = 0

while elves_energy and materials:
    third_day = False
    fifth_day = False
    count += 1

    if elves_energy[0] < 5:
        elves_energy.popleft()
        continue

    if count % 3 == 0:
        third_day = True

    if count % 5 == 0:
        fifth_day = True

    if elves_energy[0] >= materials[-1] and not third_day:
        total_energy += materials[-1]
        if not fifth_day:
            elves_energy[0] -= materials.pop() - 1
            elves_energy.append(elves_energy.popleft())
            number_of_toys += 1
        else:
            elves_energy[0] -= materials.pop()
            elves_energy.append(elves_energy.popleft())
    elif elves_energy[0] >= 2 * materials[-1] and third_day:
        total_energy += materials[-1] * 2
        if not fifth_day:
            elves_energy[0] -= (2 * materials.pop()) - 1
            elves_energy.append(elves_energy.popleft())
            number_of_toys += 2
        else:
            elves_energy[0] -= 2 * materials.pop()
            elves_energy.append(elves_energy.popleft())
    else:
        elves_energy.append(elves_energy.popleft() * 2)


print(f"Toys: {number_of_toys}")
print(f'Energy: {total_energy}')

if elves_energy:
    print(f'Elves left: {", ".join(map(str, elves_energy))}')

if materials:
    print(f'Boxes left: {", ".join(map(str, materials))}')

