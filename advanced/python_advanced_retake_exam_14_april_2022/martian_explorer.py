def movement(direction):
    if direction == 'up':
        direction_row = -1
        direction_col = 0
    elif direction == 'down':
        direction_row = 1
        direction_col = 0
    elif direction == 'left':
        direction_row = 0
        direction_col = -1
    elif direction == 'right':
        direction_row = 0
        direction_col = 1

    return direction_row, direction_col

def message(row, col, material):
    if material == 'W':
        material = "Water"
    elif material == "M":
        material = "Metal"
    elif material == "C":
        material = "Concrete"
    return f'{material} deposit found at ({row}, {col})'

size = 6

matrix = [input().split() for _ in range(6)]
commands = input().split(', ')

current_row = 0
current_col = 0

deposit_dict = {
    "W": 0,
    "M": 0,
    "C": 0
}

for r in range(len(matrix)):
    if 'E' in matrix[r]:
        c = matrix[r].index('E')
        current_row = r
        current_col = c
        break

# print(current_row, current_col)

for command in commands:
    movement_row, movement_col = movement(command)
    current_row += movement_row
    current_col += movement_col

    if current_row < 0:
        current_row = size - 1
    if current_row == size:
        current_row = 0
    if current_col < 0:
        current_col = size - 1
    if current_col == size:
        current_col = 0

    # print(current_row, current_col)
    if matrix[current_row][current_col] == "W":
        deposit_dict["W"] += 1
        print(message(current_row, current_col, matrix[current_row][current_col]))
    elif matrix[current_row][current_col] == "M":
        deposit_dict["M"] += 1
        print(message(current_row, current_col, matrix[current_row][current_col]))
    elif matrix[current_row][current_col] == "C":
        deposit_dict["C"] += 1
        print(message(current_row, current_col, matrix[current_row][current_col]))
    elif matrix[current_row][current_col] == "R":
        print(f"Rover got broken at ({current_row}, {current_col})")
        break

if deposit_dict["W"] > 0 and deposit_dict["M"] > 0 and deposit_dict["C"] > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")