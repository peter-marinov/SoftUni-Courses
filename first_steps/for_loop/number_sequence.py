import sys

num = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize
# print(max_number)
# print(min_number)
for i in range (num): # range(0, num)
    value = int(input())
    if max_number < value:
        max_number = value
    if value < min_number:
        min_number = value

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")