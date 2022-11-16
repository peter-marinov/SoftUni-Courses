size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(input()))

target_char = input()

found = False

for row in range(size):
    for col in range(size):
        if matrix[row][col] == target_char:
            print(f'({row}, {col})')
            found = True
            break
        if found:
            break

if not found:
    print(f"{target_char} does not occur in the matrix")