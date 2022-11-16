def sum_numbers(first_num: int, second_num: int):
    return first_num + second_num


def subtract(sum: int, third_num: int):
    return sum - third_num


first_number = int(input())
second_number = int(input())
third_number = int(input())

sum_numbers_result = sum_numbers(first_number, second_number)
final_result = subtract(sum_numbers_result, third_number)
print(final_result)