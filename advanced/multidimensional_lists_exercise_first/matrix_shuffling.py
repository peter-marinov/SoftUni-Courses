rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(list(input().split()))

while True:
    command = input().split()
    if 'END' in command:
        break

    if "swap" in command:
        if len(command) != 5:
            print("Invalid input!")
        else:
            row_1, col_1 = int(command[1]), int(command[2])
            row_2, col_2 = int(command[3]), int(command[4])
            # if row_1 in range(0, rows + 1) and col_1 in range(0, columns + 1) and \
            #         row_2 in range(0, rows + 1) and col_2 in range(0, columns + 1):
            if 0 <= row_1 <= rows and 0 <= col_1 <= columns and \
               0 <= row_2 <= rows and 0 <= col_2 <= columns:
                matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
                for row in range(rows):
                    print(' '.join(matrix[row]))
            else:
                print("Invalid input!")
    else:
        print("Invalid input!")
