rows = int(input())

matrix = [list(map(int, input().split())) for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == 'END':
        for row in range(rows):
            print(' '.join(map(str, matrix[row])))
        break

    action = command[0]
    first_idx, second_idx, value = list(map(int, command[1:]))
    if 0 <= first_idx < len(matrix) and 0 <= second_idx < len(matrix):
        if action == 'Add':
            matrix[first_idx][second_idx] += value
        elif action == 'Subtract':
            matrix[first_idx][second_idx] -= value
    else:
        print("Invalid coordinates")

