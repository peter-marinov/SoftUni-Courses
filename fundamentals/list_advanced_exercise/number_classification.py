def positive_numbers(numbers):
    return [num for num in numbers if int(num) >= 0]


def negative_numbers(numbers):
    return [num for num in numbers if int(num) < 0]


def even_numbers(numbers):
    return [num for num in numbers if int(num) % 2 == 0]


def odd_numbers(numbers):
    return [num for num in numbers if int(num) % 2 != 0]

numbers = input().split(', ')

# positive_numbers = [num for num in numbers if num >= 0]
# negative_numbers = [num for num in numbers if num < 0]
# even_numbers = [num for num in numbers if num % 2 == 0]
# odd_numbers = [num for num in numbers if num % 2 != 0]
# print(positive_numbers)
# print(negative_numbers)
# print(even_numbers)
# print(odd_numbers)

print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")

