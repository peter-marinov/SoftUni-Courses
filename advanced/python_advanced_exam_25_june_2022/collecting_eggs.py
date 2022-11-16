from collections import deque

eggs = deque(map(int, input().split(', ')))
paper_stack = list(map(int, input().split(', ')))

box_size = 50
filled_boxes = 0

while eggs and paper_stack:
    if eggs[0] <= 0:
        eggs.popleft()
        continue

    if eggs[0] == 13:
        eggs.popleft()
        first_paper = paper_stack[0]
        last_paper = paper_stack[-1]
        paper_stack = [last_paper] + paper_stack[1:-1] + [first_paper]
        continue

    paper_egg_size = eggs[0] + paper_stack[-1]
    if paper_egg_size <= box_size:
        filled_boxes += 1
        eggs.popleft()
        paper_stack.pop()
    else:
        eggs.popleft()
        paper_stack.pop()

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")

if paper_stack:
    print(f"Pieces of paper left: {', '.join(map(str, paper_stack))}")