'''

a = []

matrix = []
for _ in range(3):
    row = []
    for i in range(3):
        row.append(i)
    matrix.append(row)

print(matrix)
'''

'''
matrix = [[i for i in range(0, 4)] for _ in range(3)]
print(matrix)
'''

matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for sublist in matrix for num in sublist]
print(flattened)

print(ord('A'))