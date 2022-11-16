first_number = int(input())
second_number = int(input())
third_number = int(input())

def smallest_number(input_first_number, input_second_number, input_third_number):
    list_nums = []
    list_nums.append(input_first_number)
    list_nums.append(input_second_number)
    list_nums.append(input_third_number)
    # print(list_nums)
    return min(list_nums)

print(smallest_number(first_number, second_number, third_number))

