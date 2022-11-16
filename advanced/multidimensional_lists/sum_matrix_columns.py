rows, columns = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(' ')])


for column_idx in range(columns):
    current_column_sum = 0
    for row_idx in range(rows):
        current_column_sum += matrix[row_idx][column_idx]

    print(current_column_sum)

