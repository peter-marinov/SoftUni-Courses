from collections import deque

kids = deque(input().split())

number = int(input())

counter = 1
while len(kids) > 1:
    kid = kids.popleft()
    if counter == number:
        print(f"Removed {kid}")
        counter = 1
    else:
        counter += 1
        kids.append(kid)

winner = kids.popleft()
print(f"Last is {winner}")