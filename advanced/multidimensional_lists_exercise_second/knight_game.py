
'''
0K0K0
K000K
00K00
K000K
0K0K0
'''

size = int(input())

matrix = [list(input()) for _ in range(size)]

positions = (
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):
            attacks = 0
            if matrix[row][col] == 'K':
                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == 'K':
                            attacks += 1

            if attacks > max_attacks:
                knight_with_most_attacks_pos = [row, col]
                max_attacks = attacks

    if knight_with_most_attacks_pos:
        matrix[knight_with_most_attacks_pos[0]][knight_with_most_attacks_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)