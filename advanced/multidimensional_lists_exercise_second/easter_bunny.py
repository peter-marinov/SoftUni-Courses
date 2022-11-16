import sys
rows = int(input())

direction = ''
collected_eggs = -int(sys.maxsize)
collected_eggs_matrix = []


matrix = [input().split() for _ in range(rows)]

bunny_row_idx,  bunny_col_idx = [(index, row.index('B')) for index, row in enumerate(matrix) if 'B' in row][0]

# we have 4 possible directions
for current_direction in ['up', 'down', 'left', 'right']:
    current_collected_eggs = 0
    current_matrix = []
    if current_direction == 'up':
        if 0 <= bunny_row_idx - 1 < bunny_row_idx:
            for current_idx in range(bunny_row_idx - 1, -1, -1):
                if matrix[current_idx][bunny_col_idx] == 'X':
                    break
                current_collected_eggs += int(matrix[current_idx][bunny_col_idx])
                current_matrix.append([current_idx, bunny_col_idx])
            if current_collected_eggs > collected_eggs:
                collected_eggs = current_collected_eggs
                collected_eggs_matrix = current_matrix
                direction = current_direction
    elif current_direction == 'down':
        if bunny_row_idx + 1 <= rows - 1:
            for current_idx in range(bunny_row_idx + 1, rows):
                if matrix[current_idx][bunny_col_idx] == 'X':
                    break
                current_collected_eggs += int(matrix[current_idx][bunny_col_idx])
                current_matrix.append([current_idx, bunny_col_idx])
            if current_collected_eggs > collected_eggs:
                collected_eggs = current_collected_eggs
                collected_eggs_matrix = current_matrix
                direction = current_direction
    elif current_direction == 'left':
        if 0 <= bunny_col_idx - 1 < bunny_col_idx:
            for current_idx in range(bunny_col_idx - 1, -1, -1):
                if matrix[bunny_row_idx][current_idx] == 'X':
                    break
                current_collected_eggs += int(matrix[bunny_row_idx][current_idx])
                current_matrix.append([bunny_row_idx, current_idx])
            if current_collected_eggs > collected_eggs:
                collected_eggs = current_collected_eggs
                collected_eggs_matrix = current_matrix
                direction = current_direction
    elif current_direction == 'right':
        if bunny_col_idx + 1 <= rows - 1:
            for current_idx in range(bunny_col_idx + 1, rows):
                if matrix[bunny_row_idx][current_idx] == 'X':
                    break
                current_collected_eggs += int(matrix[bunny_row_idx][current_idx])
                current_matrix.append([bunny_row_idx, current_idx])
            if current_collected_eggs > collected_eggs:
                collected_eggs = current_collected_eggs
                collected_eggs_matrix = current_matrix
                direction = current_direction

print(direction)
for item in collected_eggs_matrix:
    print(item)
print(collected_eggs)
