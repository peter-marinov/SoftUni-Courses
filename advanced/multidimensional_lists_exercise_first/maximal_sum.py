import sys

rows, columns = list(map(int, input().split()))

matrix = []
max_sum = -int(sys.maxsize)
max_matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

if rows >= 3 and columns >= 3:
    for row in range(rows - 2):
        current_sum = 0
        for col in range(columns - 2):
            current_sum = matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] + \
                          matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2] + \
                          matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]

            if current_sum > max_sum:
                max_sum = current_sum
                max_matrix = [[matrix[row][col], matrix[row][col+1], matrix[row][col+2]],
                              [matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]],
                              [matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]]

print(f"Sum = {max_sum}")
if max_matrix:
    for row in range(3):
        print(' '.join(map(str, max_matrix[row])))


# rows, cols = tuple(map(int, input().split()))
# matrix = [input().split() for i in range(rows)]
#
# biggest_square = []
# biggest_square_sum = 0
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
