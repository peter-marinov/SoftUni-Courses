rows = int(input())

matrix = []
primary_diagonal_numbers = []
secondary_diagonal_numbers = []
primary_diagonal_sum = 0
secondary_diagonal_sum = 0


for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for index in range(rows):
    primary_diagonal_numbers.append(matrix[index][index])
    primary_diagonal_sum += matrix[index][index]
    secondary_diagonal_numbers.append(matrix[index][rows - 1 - index])
    secondary_diagonal_sum += matrix[index][rows - 1 - index]

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal_numbers))}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal_numbers))}. Sum: {secondary_diagonal_sum}")
