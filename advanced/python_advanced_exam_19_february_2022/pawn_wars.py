def diagonal_attack(row, col, board, color, board_size):
    if color == 'White':
        opponent = 'b'
        if col == 0:
            if board[row - 1][col + 1] == opponent:
                chess_row, chess_col = remap(row - 1, col + 1)
                print(f'Game over! {color} win, capture on {chess_col + chess_row}.')
                return True
        elif col == board_size - 1:
            if board[row - 1][col - 1] == opponent:
                chess_row, chess_col = remap(row - 1, col - 1)
                print(f'Game over! {color} win, capture on {chess_col + chess_row}.')
                return True
        else:
            if board[row - 1][col + 1] == opponent:
                chess_row, chess_col = remap(row - 1, col + 1)
                print(f'Game over! {color} win, capture on {chess_col + chess_row}.')
                return True
            elif board[row - 1][col - 1] == opponent:
                chess_row, chess_col = remap(row - 1, col - 1)
                print(f'Game over! {color} win, capture on {chess_col + chess_row}.')
                return True
    elif color == 'Black':
        opponent = 'w'
        if col == 0:
            if board[row + 1][col + 1] == opponent:
                chess_row, chess_col = remap(row + 1, col + 1)
                print(f'Game over! {color} win, capture on {chess_col + chess_row}.')
                return True
        elif col == board_size - 1:
            if board[row + 1][col - 1] == opponent:
                chess_row, chess_col = remap(row + 1, col - 1)
                print(f'Game over! {color} win, capture on {chess_col + chess_row}.')
                return True
        else:
            if board[row + 1][col + 1] == opponent:
                chess_row, chess_col = remap(row + 1, col + 1)
                print(f'Game over! {color} win, capture on {chess_col + chess_row}.')
                return True
            elif board[row + 1][col - 1] == opponent:
                chess_row, chess_col = remap(row + 1, col - 1)
                print(f'Game over! {color} win, capture on {chess_col + chess_row}.')
                return True
    return False


def remap(row, col):
    row_dict = {
        0: 8,
        1: 7,
        2: 6,
        3: 5,
        4: 4,
        5: 3,
        6: 2,
        7: 1
    }

    col_dict = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h'
    }

    row = str(row_dict[row])
    col = str(col_dict[col])

    return row, col

size = 8

matrix = []
white_pawn = []
black_pawn = []
empty_space = '-'
white_pawn_space = 'w'
black_pawn_space = 'b'
for r in range(size):
    matrix.append(input().split())
    if 'w' in matrix[r]:
        c = matrix[r].index('w')
        white_pawn = [r, c]
    if 'b' in matrix[r]:
        c = matrix[r].index('b')
        black_pawn = [r, c]

for _ in range(size):
    # White on the move
    if diagonal_attack(white_pawn[0], white_pawn[1], matrix, 'White', size):
        break

    matrix[white_pawn[0]][white_pawn[1]] = empty_space
    white_pawn[0] -= 1
    matrix[white_pawn[0]][white_pawn[1]] = white_pawn_space
    # Todo check if we have the pawn on the last space
    if white_pawn[0] == 0:
        winning_row, winning_col = remap(white_pawn[0], white_pawn[1])
        print(f"Game over! White pawn is promoted to a queen at {winning_col + winning_row}.")
        break

    # Black on the move
    if diagonal_attack(black_pawn[0], black_pawn[1], matrix, 'Black', size):
        break

    matrix[black_pawn[0]][black_pawn[1]] = empty_space
    black_pawn[0] += 1
    matrix[black_pawn[0]][black_pawn[1]] = black_pawn_space
    # Todo check if we have the pawn on the last space
    if black_pawn[0] == size - 1:
        winning_row, winning_col = remap(black_pawn[0], black_pawn[1])
        print(f"Game over! Black pawn is promoted to a queen at {winning_col + winning_row}.")
        break
