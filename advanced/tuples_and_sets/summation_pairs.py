'''
numbers = list(map(int, input().split()))
second_numbers = numbers.copy()
target = int(input())
# print(numbers)
for number in numbers:
    if len(numbers) > 1:
        # second_numbers = numbers[1:]
        second_numbers = second_numbers[1:]
        for second in second_numbers:
            if number + second == target:

                print(f"{number} + {second} = {target}")
                second_numbers.remove(second)
                # numbers.remove(second)
                # print(numbers)
                # print(second_numbers)
                # second_numbers.remove(second)
                break
'''
'''
# Solution 1
import time

start = time.time()
numbers = list(map(int, input().split()))
target = int(input())

for i in range(len(numbers)):
    if numbers[i] == '':
        continue
    for j in range(i + 1, len(numbers)):
        if numbers[j] == '':
            continue
        if numbers[i] + numbers[j] == target:
            print(f'{numbers[i]} + {numbers[j]} = {target}')
            numbers[i] = ''
            numbers[j] = ''
            break
end = time.time()
print(f"Time range {end - start}")
'''
# Solution 2
import time

numbers = list(map(int, input().split()))
target = int(input())
start = time.time()
targets = set()
values_map = {}

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f'{pair} + {value} = {target}')
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        values_map[resulting_number] = value

end = time.time()
print(f"Sim time: {end - start}")