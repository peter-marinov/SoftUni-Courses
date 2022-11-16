size = int(input())

matrix = []
position = []
for r in range(size):
    matrix.append(input().split())
    if 'P' in matrix[r]:
        c = matrix[r].index('P')
        position = [r, c]

coordinates = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

player_path = [[position[0], position[1]]]

collected_coins = 0

while True:
    command = input()
    if command not in coordinates.keys():
        continue

    position[0] += coordinates[command][0]
    position[1] += coordinates[command][1]

    if position[0] < 0:
        position[0] = size - 1
    elif position[0] == size:
        position[0] = 0

    if position[1] < 0:
        position[1] = size - 1
    elif position[1] == size:
        position[1] = 0

    player_path.append([position[0], position[1]])

    if matrix[position[0]][position[1]].isdigit():
        collected_coins += int(matrix[position[0]][position[1]])
        matrix[position[0]][position[1]] = '-'
        if collected_coins >= 100:
            print(f"You won! You've collected {collected_coins} coins.")

            break
    elif matrix[position[0]][position[1]] == 'X':
        collected_coins = collected_coins // 2
        print(f"Game over! You've collected {collected_coins} coins.")

        break

print('Your path:')
for row in player_path:
    print(row)




