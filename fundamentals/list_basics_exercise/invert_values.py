numbers = input()

list_numbers = numbers.split(' ')
final_list = []
for number in list_numbers:
    # final_list.append(int(number) * -1)
    final_list.append(-int(number))
print(final_list)