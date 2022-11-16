"""
from collections import deque

number_of_pumps = int(input())
pumps = deque()
truck_tank = 0
pumps_visited = 1
current_pump = 0
for _ in range(number_of_pumps):
    petrol_amount, distance = list(map(int, input().split()))
    pumps.append({'petrol_amount': petrol_amount, 'distance': distance})

# print(pumps[0])
while True:
    if (truck_tank + pumps[0]['petrol_amount']) >= pumps[0]['distance']:
        truck_tank += pumps[0]['petrol_amount'] - pumps[0]['distance']
        pumps_visited += 1
        if pumps_visited == number_of_pumps:
            print(f'{current_pump}')
            break
    else:
        pumps_visited = 1
        current_pump += 1
        truck_tank = 0

    shifted_pump = pumps.popleft()
    pumps.append(shifted_pump)
"""

from collections import deque

number = int(input())
total_fuel = 0
stops = 0
que = deque()
visited_stops = 0

for _ in range(number):
    que.append(input())

original_que = que
while que:
    if stops == len(que):
        print(original_que.index(que[0]))
        break
    for _ in range(number):
        fuel, distance = que[position].split()
        total_fuel += int(fuel)

        if total_fuel >= int(distance):
            total_fuel -= int(distance)
            stops += 1
        else:
            que.append(que.popleft())
            total_fuel = 0
            stops = 0
            break


