'''
from collections import deque

chocolates_stack = list(map(int, input().split(', ')))
cup_of_milks_deque = deque(map(int, input().split(', ')))

number_of_milk_shakes = 0
while True:
    if number_of_milk_shakes == 5 or len(chocolates_stack) == 0 or len(cup_of_milks_deque) == 0:
        break

    if chocolates_stack[-1] <= 0 or cup_of_milks_deque[0] <= 0:
        if chocolates_stack[-1] <= 0:
            chocolates_stack.pop()
        if cup_of_milks_deque[0] <= 0:
            cup_of_milks_deque.popleft()
        continue

    if chocolates_stack[-1] == cup_of_milks_deque[0]:
        number_of_milk_shakes += 1
        chocolates_stack.pop()
        cup_of_milks_deque.popleft()
    else:
        cup_of_milks_deque.append(cup_of_milks_deque.popleft())
        chocolates_stack[-1] -= 5

if number_of_milk_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolates_stack) > 0:
    print(f"Chocolate: {', '.join(map(str, chocolates_stack))}")
else:
    print("Chocolate: empty")

if len(cup_of_milks_deque) > 0:
    print(f"Milk: {', '.join(map(str, cup_of_milks_deque))}")
else:
    print("Milk: empty")
'''
import collections
from collections import deque

chocolates = list(map(int, input().split(', ')))
milk_cups = deque(map(int, input().split(', ')))

milkshakes = 0

while milkshakes < 5 and chocolates and milk_cups:
    flag = False
    if chocolates[-1] <= 0:
        chocolates.pop()
        flag = True

    if milk_cups[0] <= 0:
        milk_cups.popleft()
        flag = True

    if flag:
        continue

    if chocolates[-1] == milk_cups[0]:
        milkshakes += 1
        chocolates.pop()
        milk_cups.popleft()
    else:
        milk_cups.append(milk_cups.popleft())
        chocolates[-1] -= 5

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
print(f"Milk: {', '.join(map(str, milk_cups)) if milk_cups else 'empty'}")