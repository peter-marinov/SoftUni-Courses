def start():
    for row in range(size):
        for col in range(size):
            if board[row][col] == 'Q':
                # check each coordinate
                for coordinate in coordinates:
                    current_row = row
                    current_col = col
                    # while all fields are checked
                    while True:
                        current_row += coordinate[0]
                        current_col += coordinate[1]
                        if current_row in range(size) and current_col in range(size):
                            if board[current_row][current_col] == 'Q':
                                break
                            elif board[current_row][current_col] == 'K':
                                found_queens.append([row, col])
                        else:
                            break

    if found_queens:
        print(*found_queens, sep='\n')
    else:
        print('The king is safe!')


size = 8

board = [input().split() for _ in range(size)]

found_queens = []

coordinates = (
    (-1, 0),    # up
    (1, 0),     # down
    (0, -1),    # left
    (0, 1),     # right
    (-1, -1),   # up left
    (1, 1),     # down right
    (-1, 1),    # up right
    (1, -1)     # down left
)

start()

