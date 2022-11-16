rows = int(input())

matrix = [input().split() for _ in range(rows)]

alice_row_idx,  alice_col_idx = [(index, row.index('A')) for index, row in enumerate(matrix) if 'A' in row][0]
matrix[alice_row_idx][alice_col_idx] = '*'

bag_of_teas = 0
is_party = True

while bag_of_teas < 10:
    command = input()
    if command == 'up':
        alice_row_idx -= 1
        if 0 <= alice_row_idx:
            if matrix[alice_row_idx][alice_col_idx] == 'R':
                is_party = False
            elif matrix[alice_row_idx][alice_col_idx] != '.' and matrix[alice_row_idx][alice_col_idx] != '*':
                bag_of_teas += int(matrix[alice_row_idx][alice_col_idx])
            matrix[alice_row_idx][alice_col_idx] = '*'
        else:
            is_party = False
    elif command == 'down':
        alice_row_idx += 1
        if alice_row_idx <= rows - 1:
            if matrix[alice_row_idx][alice_col_idx] == 'R':
                is_party = False
            elif matrix[alice_row_idx][alice_col_idx] != '.' and matrix[alice_row_idx][alice_col_idx] != '*':
                bag_of_teas += int(matrix[alice_row_idx][alice_col_idx])
            matrix[alice_row_idx][alice_col_idx] = '*'
        else:
            is_party = False
    elif command == 'left':
        alice_col_idx -= 1
        if 0 <= alice_col_idx:
            if matrix[alice_row_idx][alice_col_idx] == 'R':
                is_party = False
            elif matrix[alice_row_idx][alice_col_idx] != '.' and matrix[alice_row_idx][alice_col_idx] != '*':
                bag_of_teas += int(matrix[alice_row_idx][alice_col_idx])
            matrix[alice_row_idx][alice_col_idx] = '*'
        else:
            is_party = False
    elif command == 'right':
        alice_col_idx += 1
        if alice_col_idx <= rows - 1:
            if matrix[alice_row_idx][alice_col_idx] == 'R':
                is_party = False
            elif matrix[alice_row_idx][alice_col_idx] != '.' and matrix[alice_row_idx][alice_col_idx] != '*':
                bag_of_teas += int(matrix[alice_row_idx][alice_col_idx])
            matrix[alice_row_idx][alice_col_idx] = '*'
        else:
            is_party = False

    if not is_party:
        print("Alice didn't make it to the tea party.")
        break

if is_party:
    print("She did it! She went to the party.")
for row in range(rows):
    print(' '.join(map(str, matrix[row])))