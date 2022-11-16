def naughty_or_nice_list(*args, **kwargs):
    kids_dict = {
        'Nice': [],
        'Naughty': [],
        'Not found': []
    }
    current_kids = []
    kids = [list(kid) for kid in args[0]]
    commands = list(args[1:])
    for command in commands:
        command = command.split('-')
        number, status = int(command[0]), command[1]
        for kid in kids:
            kid_number, kid_name = kid
            if number == kid_number:
                current_kids.append([status, number, kid_name])
        if len(current_kids) == 1:
            kids_dict[current_kids[0][0]].append(current_kids[0][2])
            kids.remove([current_kids[0][1], current_kids[0][2]])
        current_kids = []

    for key, value in kwargs.items():
        for kid in kids:
            kid_number, kid_name = kid
            if key == kid_name:
                current_kids.append([value, kid_number, kid_name])
        if len(current_kids) == 1:
            kids_dict[current_kids[0][0]].append(current_kids[0][2])
            kids.remove([current_kids[0][1], current_kids[0][2]])
        current_kids = []

    if kids:
        for kid in kids:
            kids_dict['Not found'].append(kid[1])

    result = ''

    for key, value in kids_dict.items():
        if value:
            result += f'{key}: {", ".join(value)}\n'
    return result

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))