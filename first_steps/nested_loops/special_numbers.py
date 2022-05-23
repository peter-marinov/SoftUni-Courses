number = int(input())

all_numbers_divided = True
for special_number in range(1111, 9999 + 1):
    special_number_str = str(special_number)
    for index, value in enumerate(special_number_str):
        if int(value) == 0:
            all_numbers_divided = False
            break
        elif number % int(value) != 0:
            all_numbers_divided = False
            break

    if all_numbers_divided:
        print(special_number, end=" ")
    else:
        all_numbers_divided = True