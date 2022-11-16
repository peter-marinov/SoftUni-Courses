text = input()

size = int(input())

matrix = []
player_position = []

for r in range(size):
    matrix.append(list(input()))
    if 'P' in matrix[r]:
        c = matrix[r].index('P')
        player_position = [r, c]

coordinates = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

lines = int(input())

for _ in range(lines):
    command = input()
    if player_position[0] + coordinates[command][0] not in range(size):
        text = text[:-1]
        continue

    if player_position[1] + coordinates[command][1] not in range(size):
        text = text[:-1]
        continue

    matrix[player_position[0]][player_position[1]] = '-'
    player_position[0] += coordinates[command][0]
    player_position[1] += coordinates[command][1]
    if matrix[player_position[0]][player_position[1]] != '-':
        text += matrix[player_position[0]][player_position[1]]
    matrix[player_position[0]][player_position[1]] = 'P'

print(text)
for row in range(size):
    print(''.join(matrix[row]))
