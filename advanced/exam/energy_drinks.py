from collections import deque
milligrams_of_caffeine = list(map(int, input().split(',')))
energy_drinks = deque(map(int, input().split(',')))


maximum_caffeine = 300
current_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    caffeine = milligrams_of_caffeine[-1] * energy_drinks[0]
    if current_caffeine + caffeine <= maximum_caffeine:
        milligrams_of_caffeine.pop()
        energy_drinks.popleft()
        current_caffeine += caffeine
    else:
        milligrams_of_caffeine.pop()
        energy_drinks.append(energy_drinks.popleft())
        current_caffeine -= 30
        if current_caffeine < 0:
            current_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")