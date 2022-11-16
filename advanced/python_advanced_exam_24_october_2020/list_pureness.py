def best_list_pureness(*args):
    iterations = args[-1]
    numbers = args[:-1][0]
    rotations = []

    for _ in range(iterations + 1):
        current_sum = sum([number * numbers.index(number) for number in numbers])
        rotations.append(current_sum)
        numbers.insert(0, numbers.pop())

    return f"Best pureness {max(rotations)} after {rotations.index(max(rotations))} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)