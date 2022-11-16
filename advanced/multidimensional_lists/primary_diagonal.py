matrix_size = int(input())

matrix = []
for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

total = 0
for index in range(matrix_size):
    total += matrix[index][index]

print(total)