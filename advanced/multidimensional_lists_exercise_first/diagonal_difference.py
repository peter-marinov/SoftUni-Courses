rows = int(input())

matrix = []

primary_diagonal_sum = 0
secondary_diagonal_sum = 0


for _ in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

for index in range(rows):
    primary_diagonal_sum += matrix[index][index]
    secondary_diagonal_sum += matrix[index][rows - 1 - index]

result = abs(primary_diagonal_sum - secondary_diagonal_sum)
print(result)
