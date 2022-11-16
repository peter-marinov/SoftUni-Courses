# command = input().split()
#
# sum = 0
#
# for symbol_first in command[0]:
#     for symbol_second in command[1]:
#         sum += ord(symbol_first) * ord(symbol_second)
#         print(sum)
#
# print(sum)

first_string, second_string = input().split()
total_sum = 0
deference = abs(len(first_string) - len(second_string))
if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string) - deference, len(first_string)):
        total_sum += ord(first_string[index])
elif len(first_string) < len(second_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
elif len(first_string) == len(second_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])

print(total_sum)


