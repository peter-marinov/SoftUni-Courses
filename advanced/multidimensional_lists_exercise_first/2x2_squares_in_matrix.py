rows, columns = list(map(int, input().split()))

matrix = []
counter = 0

for _ in range(rows):
    matrix.append(list(input().split()))

for row in range(rows - 1):
    for col in range(columns - 1):
        if all(symbol == matrix[row][col] for symbol in [matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]]):
            counter += 1


print(counter)
