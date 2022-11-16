is_number_in_range = False

while not is_number_in_range:
    number = float(input())
    if 1 <= number and number <= 100:
        print(f'The number {number} is between 1 and 100')
        is_number_in_range = True

