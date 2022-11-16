def check_the_throw(bucket, row, col, number_of_points, bucket_size):

    if 0 <= row < bucket_size and 0 <= col < bucket_size:
        if bucket[row][col] == 'B':
            for r in range(bucket_size):
                if bucket[r][col] != 'B':
                    number_of_points += int(bucket[r][col])
            # number_of_points += sum([int(bucket[r][col]) for r in range(row-1, -1, -1)])
            bucket[row][col] = 'X'
    return bucket, number_of_points


size = 6

matrix = [input().split() for _ in range(size)]
number_of_throws = 3
points = 0
for _ in range(number_of_throws):
    coordinates = tuple(map(int, input()[1:-1].split(', ')))
    matrix, points = check_the_throw(matrix, coordinates[0], coordinates[1], points, size)


if points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
elif points >= 200:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points >= 100:
    print(f"Good job! You scored {points} points, and you've won Football.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")

