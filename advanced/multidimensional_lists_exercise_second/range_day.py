def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < size and 0 <= c < size):
        return my_position

    if field[r][c] == 'x':
        return my_position

    return [r, c]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]

size = 5
field = []

targets = 0
targets_hit = 0
target_hit_positions = []

my_position = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()

    field.append(line)

    if 'A' in line:
        my_position = [row, line.index('A')]
        field[row][my_position[1]] = '.'

    targets += line.count('x')

for _ in range(int(input())):
    command_info = input().split()

    if command_info[0] == 'move':
        my_position = move(command_info[1], int(command_info[2]))
    elif command_info[0] == 'shoot':
        target_down_pos = shoot(command_info[1])

        if target_down_pos:
            target_hit_positions.append(target_down_pos)
            targets_hit += 1

        if targets_hit == targets:
            print(f"Training completed! All {targets} targets hit.")
            break


if targets_hit < targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")

[print(target_pos) for target_pos in target_hit_positions]