from collections import deque

people = deque()
while True:
    line = input()
    if line == 'End':
        break

    if line == 'Paid':
        print('\n'.join(people))
        people.clear()
    else:
        people.append(line)

print(f'{len(people)} people remaining.')

