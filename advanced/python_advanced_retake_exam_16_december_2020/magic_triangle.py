from math import ceil


def get_magic_triangle(number):
    matrix = [[1], [1, 1]]
    if number > 2:
        for row in range(3, number + 1):
            new_list = [0] * row
            new_list[0] = 1
            for index in range(0, len(matrix[row - 2])):
                if index + 1 <= row - 2:
                    new_list[index + 1] += matrix[row - 2][index] + matrix[row - 2][index + 1]
                else:
                    new_list[-1] = 1


            matrix.append(new_list)

    # print(matrix)
    return matrix


get_magic_triangle(5)

