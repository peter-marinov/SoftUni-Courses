def numbers_searching(*args):
    numbers = list(args)
    numbers.sort()
    result = []

    found_numbers = []
    for number in numbers:
        if number + 1 not in numbers and number != numbers[-1]:
            result = [number + 1]
        if numbers.count(number) > 1:
            if number not in found_numbers:
                found_numbers.append(number)
    result.append(found_numbers)
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))