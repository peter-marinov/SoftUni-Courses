from collections import deque

customers = deque(map(int, input().split(', ')))
taxis = list(map(int, input().split(', ')))

time_spent = 0

while customers and taxis:
    if taxis[-1] >= customers[0]:
        time_spent += customers.popleft()

    taxis.pop()

if customers:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(map(str, customers))}')
else:
    print(f'All customers were driven to their destinations')
    print(f'Total time: {time_spent} minutes')