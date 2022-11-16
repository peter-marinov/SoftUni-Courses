"""clothes = list(map(int, input().split()))
rack_capacity = int(input())
if clothes:
    number_of_racks = 1
else:
    number_of_racks = 0

current_rack_capacity = 0
while clothes:
    if current_rack_capacity + clothes[-1] < rack_capacity:
        current_rack_capacity += clothes.pop()
    elif current_rack_capacity + clothes[-1] == rack_capacity:
        clothes.pop()
        if number_of_racks != 1:
            current_rack_capacity = 0
            number_of_racks += 1
    else:
        current_rack_capacity = 0
        number_of_racks += 1

print(number_of_racks)
"""

clothes = list(map(int, input().split()))
capacity = int(input())
racks = 1

temp = 0
for _ in range(len(clothes)):
    if temp + clothes[-1] > capacity:
        racks += 1
        temp = clothes.pop()
    elif temp + clothes[-1] == capacity:
        temp = 0
        clothes.pop()
        if clothes:
            racks += 1
    else:
        temp += clothes.pop()

print(racks)