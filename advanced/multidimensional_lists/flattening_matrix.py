rows = int(input())

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

result = []
[result.extend(row) for row in matrix]
print(result)