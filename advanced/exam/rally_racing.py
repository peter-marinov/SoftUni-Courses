size = int(input())
car_number = input()

matrix = []

tunnel = []

kilometers_passed = 0
row = 0
col = 0

coordinates = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(size):
    matrix.append(input().split())
    if 'T' in matrix[r]:
        c = matrix[r].index('T')
        tunnel.append((r, c))

while True:
    command = input()
    if command == 'End':
        matrix[row][col] = 'C'
        print(f"Racing car {car_number} DNF.")
        break

    row += coordinates[command][0]
    col += coordinates[command][1]

    if matrix[row][col] == '.':
        kilometers_passed += 10
    elif matrix[row][col] == 'T':
        matrix[row][col] = '.'
        if tunnel[0] == (row, col):
            row, col = tunnel[1]
        else:
            row, col = tunnel[0]
        matrix[row][col] = '.'
        kilometers_passed += 30
    elif matrix[row][col] == 'F':
        kilometers_passed += 10
        matrix[row][col] = 'C'
        print(f'Racing car {car_number} finished the stage!')
        break

print(f"Distance covered {kilometers_passed} km." )
for row in matrix:
    print(*row, sep='')


