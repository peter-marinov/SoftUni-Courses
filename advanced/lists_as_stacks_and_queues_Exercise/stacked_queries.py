iterations = int(input())

numbers = []
numbers_revers = []

for _ in range(iterations):
    command = input().split()
    if len(command) == 2:
        numbers.append(int(command[1]))
    else:
        action = int(command[0])
        # remove top on the stack
        if numbers:
            if action == 2:
                numbers.pop()
            # print maximum number
            elif action == 3:
                print(f'{max(numbers)}')
            # print minimum number
            elif action == 4:
                print(f'{min(numbers)}')

while numbers:
    numbers_revers.append(str(numbers.pop()))

print(', '.join(numbers_revers))

