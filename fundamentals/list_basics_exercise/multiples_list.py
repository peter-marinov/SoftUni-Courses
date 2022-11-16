factor = int(input())
count = int(input())

numbers_list = []

# num = 1
#
# while True:
#     if num % factor == 0:
#         numbers_list.append(num)
#         if len(numbers_list) == count:
#             break
#     num += 1

for multiplier in range(1, count + 1):
    numbers_list.append(2 * multiplier)

print(numbers_list)