'''
from collections import deque

rows, columns = [int(x) for x in input().split()]

text = deque(input())
matrix = []
current_text = text

for row in range(rows):
    current_row = []
    for col in range(columns):
        if col <= len(current_text):
            current_row.append(current_text.popleft())
    matrix.append(current_row)
    current_text.append(text[::-1])

print(matrix)
'''

rows, cols = tuple(map(int, input().split()))

snake = input()
matrix = []
index = 0

for row in range(rows):
    result = ''
    for col in range(cols):
        result += snake[index % len(snake)]
        index += 1
        print(index % len(snake))

    if row % 2 == 0:
        matrix.append(result)
    else:
        matrix.append(result[::-1])

for submatrix in matrix:
    print(submatrix)