def list_manipulator(*args):
    numbers = args[0]
    command = args[1]

    if command == 'add':
        numbers_to_add = args[3:]
        if args[2] == 'beginning':
            for number in numbers_to_add[::-1]:
                numbers.insert(0, number)
        else:
            for number in numbers_to_add:
                numbers.append(number)

    elif command == 'remove':
        if args[-1] == 'beginning':
            numbers.pop(0)
        elif args[-1] == 'end':
            numbers.pop()
        else:
            numbers_to_remove = args[3:]
            for _ in range(numbers_to_remove[0]):
                if args[2] == 'beginning':
                    numbers.pop(0)
                else:
                    numbers.pop()

    return numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))