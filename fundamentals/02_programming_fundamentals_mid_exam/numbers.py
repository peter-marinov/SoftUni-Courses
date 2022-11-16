numbers = list(map(int, input().split()))

sorted_list = []
average_num = sum(numbers) / len(numbers)
sorted_list = [num for num in numbers if num > average_num]
if sorted_list:
    sorted_list = sorted(sorted_list, reverse=True)
    if len(sorted_list) > 5:
        sorted_list = sorted_list[0:5]
    # print(average_num)
    print(" ".join([str(num) for num in sorted_list]))
else:
    print("No")