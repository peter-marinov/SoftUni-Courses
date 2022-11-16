numbers = tuple(map(float, input().split()))

unique = []
output = {}
for number in numbers:
    if number not in unique:
        unique.append(number)

for number in unique:
    number_count = numbers.count(number)
    output[number] = str(f'{number_count} times')
    # print(f"{number} - {number_count} times")

for key, value in output.items():
    print(f'{key} - {value} times')