# from math import ceil

numbers = list(map(int, input().split(', ')))

max_number = max(numbers)

for num in range(1, max_number // 10 + 2):
    # print(max_number // 10 + 2)
    # print(num)
    current_list = [number for number in numbers if (num - 1) * 10 < number <= num * 10]
    if num == max_number // 10 + 1:
        # print("inside")
        if current_list:
            # print("vliza")
            pass
        else:
            break

    # if num == max_number // 10 + 1:
    #     print(f"Group of {num * 10}'s: {current_list}")
    #     break
    print(f"Group of {num*10}'s: {current_list}")

# for current_number in numbers:
#     for key in numbers_dict[]:
        
# print(numbers_dict)
# print(max_number // 10 + 1)