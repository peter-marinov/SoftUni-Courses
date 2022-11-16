import sys


def movement(matrix, position, direction, step):
    stop_program = False
    row, col = position
    matrix[row][col] = trail
    for _ in range(step):
        row += coordinates[direction][0]
        col += coordinates[direction][1]
        row = check_position(row, 'row')
        col = check_position(col, 'col')
        matrix = field_check(matrix, row, col)
        current_sum = sum([value for value in christmas_dict.values()])
        if current_sum == all_items:
            matrix[row][col] = santa
            print(f"Merry Christmas!")
            print_result()
            stop_program = True
            # sys.exit()
            return matrix, [row, col], stop_program

    matrix[row][col] = santa
    return matrix, [row, col], stop_program


def print_result():
    print(f"You've collected:")
    print(f"- {christmas_dict['Christmas decorations']} Christmas decorations")
    print(f"- {christmas_dict['Gifts']} Gifts")
    print(f"- {christmas_dict['Cookies']} Cookies")
    for row in board:
        print(*row, sep=' ')


def check_position(index, row_or_col):
    if row_or_col == 'row':
        if index < 0:
            index = board_rows - 1
        elif index == board_rows:
            index = 0
    else:
        if index < 0:
            index = board_cols - 1
        elif index == board_cols:
            index = 0

    return index


def field_check(matrix, row, col):
    if matrix[row][col] == 'D':
        christmas_dict['Christmas decorations'] += 1
    elif matrix[row][col] == 'G':
        christmas_dict['Gifts'] += 1
    elif matrix[row][col] == 'C':
        christmas_dict['Cookies'] += 1

    matrix[row][col] = trail
    return matrix

board_rows, board_cols = tuple(map(int, input().split(', ')))

trail = 'x'
santa = 'Y'
santa_position = []
board = []
all_items = 0

christmas_dict = {
    'Christmas decorations': 0,
    'Gifts': 0,
    'Cookies': 0
}

coordinates = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(board_rows):
    board.append(input().split())
    if 'Y' in board[r]:
        c = board[r].index('Y')
        santa_position = [r, c]
    all_items += board[r].count('D')
    all_items += board[r].count('G')
    all_items += board[r].count('C')

while True:
    command = input().split('-')

    if command[0] == 'End':
        print_result()
        break
    steps = int(command[1])

    board, santa_position, stop_program = movement(board, santa_position, command[0], steps)
    if stop_program:
        break


