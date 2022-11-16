'''
from collections import deque

bees_deque = deque(map(int, input().split()))
nectar_stack = list(map(int, input().split()))
symbols_deque = deque(input().split())

collected_honey = 0
while True:
    if len(bees_deque) == 0 or len(nectar_stack) == 0:
        break

    if nectar_stack[-1] >= bees_deque[0]:
        if symbols_deque[0] == "+":
            collected_honey += abs(bees_deque[0] + nectar_stack[-1])
        elif symbols_deque[0] == "-":
            collected_honey += abs(bees_deque[0] - nectar_stack[-1])
        elif symbols_deque[0] == "*":
            collected_honey += abs(bees_deque[0] * nectar_stack[-1])
        elif symbols_deque[0] == "/":
            if bees_deque[0] != 0 and nectar_stack[-1] != 0:
                collected_honey += abs(bees_deque[0] / nectar_stack[-1])

        bees_deque.popleft()
        nectar_stack.pop()
        symbols_deque.popleft()
    else:
        nectar_stack.pop()

print(f"Total honey made: {collected_honey}")
if bees_deque:
    print(f"Bees left: {', '.join(map(str, bees_deque))}")
if nectar_stack:
    print(f"Nectar left: {', '.join(map(str, nectar_stack))}")
'''

from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0
while bees and nectar:
    if nectar[-1] >= bees[0]:
        symbol = symbols.popleft()
        collected_nectar, bee = nectar.pop(), bees.popleft()
        if symbol == '+':
            total_honey += abs(bee + collected_nectar)
        elif symbol == '-':
            total_honey += abs(bee - collected_nectar)
        elif symbol == '*':
            total_honey += abs(bee * collected_nectar)
        elif symbol == '/':
            if collected_nectar == 0 or bee == 0:
                continue
            total_honey += abs(bee / collected_nectar)
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
