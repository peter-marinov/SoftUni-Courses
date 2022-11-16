lines = int(input())

longest_intersection = set()
for _ in range (lines):
    first_numbers, second_numbers = input().split('-')
    first_number_start, first_number_end = map(int, first_numbers.split(','))
    second_number_start, second_number_end = map(int, second_numbers.split(','))
    current_set = set(i for i in range(first_number_start, first_number_end + 1)).intersection(y for y in range(second_number_start, second_number_end + 1))
    if len(current_set) > len(longest_intersection):
        longest_intersection = current_set

numbers_output = list(longest_intersection)
# print(f'Longest intersection is {numbers_output} with length {len(numbers_output)}')
print(f"Longest intersection is [{', '.join(map(str, {i for i in longest_intersection}))}] with length {len(numbers_output)}")
