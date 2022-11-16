from math import floor

group_size = int(input())
number_of_days = int(input())

budget = 0

for day in range(1, number_of_days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    if day % 3 == 0:
        budget -= 3 * group_size
    if day % 5 == 0:
        budget += 20 * group_size
        if day % 3 == 0:
            budget -= 2 * group_size
    budget += 50 - 2 * group_size

coins_per_companion = floor(budget / group_size)

print(f'{group_size} companions received {coins_per_companion} coins each.')