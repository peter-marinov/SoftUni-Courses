from collections import deque

bomb_effects = deque(map(int, input().split(', ')))
bomb_casings = list(map(int, input().split(', ')))

bombs_dict = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0
}

while bomb_effects and bomb_casings:
    current_sum = bomb_effects[0] + bomb_casings[-1]
    if current_sum == 120:
        bombs_dict['Smoke Decoy Bombs'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif current_sum == 60:
        bombs_dict['Cherry Bombs'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif current_sum == 40:
        bombs_dict['Datura Bombs'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

    if bombs_dict['Datura Bombs'] >= 3 and bombs_dict['Cherry Bombs'] >= 3 and bombs_dict['Smoke Decoy Bombs'] >= 3:
        break

if bombs_dict['Datura Bombs'] >= 3 and bombs_dict['Cherry Bombs'] >= 3 and bombs_dict['Smoke Decoy Bombs'] >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join(map(str, bomb_effects)) if bomb_effects else 'empty'}")
print(f"Bomb Casings: {', '.join(map(str, bomb_casings)) if bomb_casings else 'empty'}")

for key, value in bombs_dict.items():
    print(f'{key}: {value}')