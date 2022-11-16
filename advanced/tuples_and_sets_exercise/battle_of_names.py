from math import floor

lines = int(input())

divider = 1
odd_set = set()
even_set = set()

for _ in range(lines):
    name = input()
    name_sum = floor(sum([ord(letter) for letter in name]) / divider)
    divider += 1
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(odd_set) == sum(even_set):
    print(', '.join(map(str, (odd_set.union(even_set)))))
elif sum(odd_set) > sum(even_set):
    print(', '.join(map(str, (odd_set.difference(even_set)))))
elif sum(odd_set) < sum(even_set):
    print(', '.join(map(str, (odd_set.symmetric_difference(even_set)))))