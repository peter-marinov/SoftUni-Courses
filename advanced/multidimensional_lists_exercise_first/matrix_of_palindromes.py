rows, columns = list(map(int, input().split()))

matrix = []
start_symbol = ord('a')
for row in range(rows):
    current_row = []
    for col in range(columns):
        string = chr(start_symbol + row) + chr(start_symbol + col + row) + chr(start_symbol + row)
        current_row.append(string)
    matrix.append(current_row)

for row in range(rows):
    print(' '.join(map(str, matrix[row])))
