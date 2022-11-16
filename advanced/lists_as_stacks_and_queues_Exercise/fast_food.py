from collections import deque

food_quantity = int(input())
orders_queued = deque(map(int, (input().split())))

print(max(orders_queued))

while orders_queued:
    if orders_queued[0] > food_quantity:
        break
    else:
        food_quantity -= orders_queued[0]
        orders_queued.popleft()

if orders_queued:
    print(f"Orders left: ", end='')
    for number in orders_queued:
        print(number, end=' ')
else:
    print("Orders complete")