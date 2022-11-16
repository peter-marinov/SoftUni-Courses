'''
rows, columns = list(map(int, input().split(', ')))

matrix = []
total_sum = 0
for _ in range(rows):
    row = list(map(int, input().split(', ')))
    total_sum += sum(row)
    matrix.append(row)

print(total_sum)
print(matrix)
'''

rows, columns = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

total = 0
for row in range(rows):
    for col in range(columns):
        total += matrix[row][col]
print(total)
print(matrix)