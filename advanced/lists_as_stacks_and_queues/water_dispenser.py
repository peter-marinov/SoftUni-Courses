from collections import deque

total_water = int(input())

people = deque()

while True:
    line = input()
    if line == "Start":
        break
    people.append(line)

while True:
    line = input()
    if line == "End":
        break

    line_args = line.split()
    # refill
    if len(line_args) == 2:
        total_water += int(line_args[1])
    # litters
    else:
        litters = int(line_args[0])
        person = people.popleft()
        if litters > total_water:
            print(f"{person} must wait")
        else:
            print(f'{person} got water')
            total_water -= litters

print(f'{total_water} liters left')