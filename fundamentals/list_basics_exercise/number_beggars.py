sums_list_as_string = input().split(', ')
count_of_beggars = int(input())

final_list = []
counter_of_index = 0
# sums_list_as_digits = [int(i) for i in sums_list]
sums_list_as_digits = []
for element in sums_list_as_string:
    sums_list_as_digits.append(int(element))

while counter_of_index < count_of_beggars:
    sum_for_current_beggar = 0
    for element in range(counter_of_index, len(sums_list_as_digits), count_of_beggars):
        sum_for_current_beggar += sums_list_as_digits[element]
    final_list.append(sum_for_current_beggar)
    counter_of_index += 1

print(final_list)

