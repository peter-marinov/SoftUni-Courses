import sys

num = int(input())

max_value = -sys.maxsize
sum_values = 0
for num in range (num):
    value = int(input())
    sum_values += value
    # print(value)
    if max_value < value:
        max_value = value

# print(max_value)
# print(sum_values)
final_sum = sum_values - max_value
if  max_value == final_sum:
    print(f"Yes\nSum = {final_sum}")
else:
    diff = abs(max_value - final_sum)
    print(f"No\nDiff = {diff}")