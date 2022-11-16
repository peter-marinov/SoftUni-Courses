from collections import deque

pizzas = deque(map(int, input().split(', ')))
workers = list(map(int, input().split(', ')))

pizzas_to_be_made = len(pizzas)
number_of_made_pizzas = 0

while pizzas and workers:
    if pizzas[0] < 1 or pizzas[0] > 10:
        pizzas.popleft()
        pizzas_to_be_made -= 1
        continue

    if workers[-1] < 1:
        workers.pop()
        continue

    if pizzas[0] <= workers[-1]:
        pizzas_to_be_made -= 1
        number_of_made_pizzas += pizzas.popleft()
        workers.pop()
    elif pizzas[0] > workers[-1]:
        done_pizzas = workers.pop()
        pizzas[0] -= done_pizzas
        number_of_made_pizzas += done_pizzas

if pizzas_to_be_made == 0:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {number_of_made_pizzas}')
    print(f'Employees: {", ".join(map(str, workers))}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(map(str, pizzas))}')
