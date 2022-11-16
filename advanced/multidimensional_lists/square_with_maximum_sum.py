rows, columns = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

max_sum = 0
max_matrix = []

for row in range(rows - 1):
    current_sum = 0
    for col in range(columns - 1 ):
        current_sum = matrix[row][col] + matrix[row][col + 1] + \
                      matrix[row + 1][col] + matrix[row+1][col + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = [[matrix[row][col], matrix[row][col + 1]],
                          [matrix[row + 1][col], matrix[row+1][col + 1]]]


for row in max_matrix:
    print(' '.join(map(str, row)))
print(max_sum)