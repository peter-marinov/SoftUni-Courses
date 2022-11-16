size = int(input())
number_of_bombs = int(input())

# board = [[0] * size] * size
board = [[0] * size]

coordinates = (
    (-1, 0),    # up
    (1, 0),     # down
    (0, -1),    # left
    (0, 1),     # right
    (-1, -1),   # up left
    (1, 1),     # down right
    (-1, 1),    # up right
    (1, -1)    # down left
)

for _ in range(size - 1):
    board.append([0] * size)

for _ in range(number_of_bombs):
    r, c = list(map(int, eval(input())))
    board[r][c] = '*'

for row in range(size):
    for col in range(size):
        if board[row][col] == '*':
            for coordinate in coordinates:
                current_row, current_col = row, col
                current_row += coordinate[0]
                current_col += coordinate[1]
                if current_row in range(size) and current_col in range(size):
                    if board[current_row][current_col] != '*':
                        board[current_row][current_col] += 1

for row in board:
    print(' '.join(map(str, row)))
