# def even_number(numbers_list):
#     even_numbers_list = []
#     for number in numbers_list:
#         if int(number) % 2 == 0:
#             even_numbers_list.append(int(number))
#     return even_numbers_list
#
# input_numbers_list = input().split(' ')
# even_list = even_number(input_numbers_list)
# print(even_list)

# numbers_as_string = input().split(' ')
# numbers_as_digits = []
# for current_number in numbers_as_string:
#     numbers_as_digits.append(int(current_number))

numbers_as_digits = [int(s) for s in input().split()]
# print(numbers_as_digits)
# filter(function, iterable_object)
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)