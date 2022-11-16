from collections import deque

ramen_stack = list(map(int, input().split(', ')))
customers_deque = deque(map(int, input().split(', ')))

que_size = len(customers_deque)
served_customers = 0

while ramen_stack and customers_deque:
    if ramen_stack[-1] == customers_deque[0]:
        ramen_stack.pop()
        customers_deque.popleft()
        served_customers += 1
    elif ramen_stack[-1] > customers_deque[0]:
        ramen_stack[-1] -= customers_deque.popleft()
        served_customers += 1
    elif ramen_stack[-1] < customers_deque[0]:
        customers_deque[0] -= ramen_stack.pop()

if served_customers == que_size:
    print("Great job! You served all the customers.")
    if ramen_stack:
        print(f"Bowls of ramen left: {', '.join(map(str, ramen_stack))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers_deque))}")
