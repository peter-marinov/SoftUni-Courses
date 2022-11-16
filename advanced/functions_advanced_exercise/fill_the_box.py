def fill_the_box(*args):
    box_space = args[0] * args[1] * args[2]
    for idx in range(3, len(args)):
        if args[idx] == 'Finish':
            if box_space > 0:
                return f'There is free space in the box. You could put {box_space} more cubes.'
            else:
                return f'No more free space! You have {abs(box_space)} more cubes.'
        else:
            box_space -= args[idx]


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))