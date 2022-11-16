size = int(input())

board = []
snake_coordinates = []
trail = '.'
food = '*'
burrow = 'B'
food_quantity = 0
burrows = []

coordinates = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(size):
    board.append(list(input()))
    if 'S' in board[r]:
        c = board[r].index('S')
        snake_coordinates = [r, c]
    if 'B' in board[r]:
        c = board[r].index('B')
        burrows.append([r, c])

current_row, current_col = snake_coordinates[0], snake_coordinates[1]
board[current_row][current_col] = trail
while food_quantity < 10:
    command = input()
    current_row += coordinates[command][0]
    current_col += coordinates[command][1]

    # if current_col not in range(size) or current_col not in range(size):
    if current_row not in range(size) or current_col not in range(size):
        break
    else:
        if board[current_row][current_col] == food:
            food_quantity += 1
        elif board[current_row][current_col] == burrow:
            board[current_row][current_col] = trail
            if burrows[0][0] == current_row and burrows[0][1] == current_col:
                current_row, current_col = burrows[1][0], burrows[1][1]
            else:
                current_row, current_col = burrows[0][0], burrows[0][1]

        if food_quantity != 10:
            board[current_row][current_col] = trail
        else:
            board[current_row][current_col] = 'S'


if food_quantity == 10:
    print('You won! You fed the snake.')
else:
    print('Game over!')

print(f'Food eaten: {food_quantity}')
for row in board:
    print(''.join(row))