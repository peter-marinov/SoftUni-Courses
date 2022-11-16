def direction(dir):
    current_row = 0
    current_col = 0

    if dir == "up":
        current_row += -1
        current_col += 0
    elif dir == "down":
        current_row += 1
        current_col += 0
    elif dir == "left":
        current_row += 0
        current_col += -1
    elif dir == "right":
        current_row += 0
        current_col += 1

    return current_row, current_col


size = 6

matrix = [input().split() for _ in range(size)]

start_row, start_col = tuple(map(int, (input()[1:-1].split(', '))))
current_row = start_row
current_col = start_col
while True:
    command = input().split(', ')
    if command[0] == 'Stop':
        break

    row, col = direction(command[1])
    current_row += row
    current_col += col
    if command[0] == "Create":
        value = command[2]
        if matrix[current_row][current_col] == '.':
            matrix[current_row][current_col] = value
            # print( matrix[current_col][current_row])
    elif command[0] == "Update":
        value = command[2]
        if matrix[current_row][current_col] != '.':
            matrix[current_row][current_col] = value
    elif command[0] == "Delete":
        if matrix[current_row][current_col] != '.':
            matrix[current_row][current_col] = '.'
    elif command[0] == "Read":
        if matrix[current_row][current_col] != '.':
            print(matrix[current_row][current_col])

for row in matrix:
    print(' '.join(row))

