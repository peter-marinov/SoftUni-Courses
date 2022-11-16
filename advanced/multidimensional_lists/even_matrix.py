rows = int(input())

result = []
for _ in range(rows):
    row = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    result.append(row)

print(result)