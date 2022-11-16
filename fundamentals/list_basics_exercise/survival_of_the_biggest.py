list_of_numbers = input().split()
number_of_small_numbers = int(input())
list_of_numbers_as_integer = []
for number in list_of_numbers:
    list_of_numbers_as_integer.append(int(number))

small_numbers = list_of_numbers_as_integer
# print(list_of_numbers_as_integer)

for remove_number in range(number_of_small_numbers):
    list_of_numbers_as_integer.remove(min(list_of_numbers_as_integer))

result = ', '.join(str(x) for x in list_of_numbers_as_integer)
# for numbers in range(len(list_of_numbers_as_integer)):
#     string_numbers = str(list_of_numbers_as_integer[numbers]) + ', '

print(result)

# list_of_numbers = input().split()
# number_of_small_numbers = int(input())
# list_of_numbers_as_integer = []
# for number in list_of_numbers:
#     list_of_numbers_as_integer.append(int(number))
#
# small_numbers = list_of_numbers_as_integer
# print(list_of_numbers_as_integer)
# small_numbers.sort()
# small_numbers = small_numbers[:number_of_small_numbers]
#
# for remove_number in small_numbers:
#     if remove_number in list_of_numbers_as_integer:
#         list_of_numbers_as_integer.remove(remove_number)
#         print(remove_number)
#         print(list_of_numbers_as_integer)
#
# print(list_of_numbers_as_integer)
#
# team_a = [1, 9, 4, 2, 0]
#
# team_a.remove(min(team_a))
# # team_a.remove(1)
#
# print(team_a)