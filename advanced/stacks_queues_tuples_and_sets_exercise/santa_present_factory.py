'''
from collections import deque

materials_stack = list(map(int, input().split()))
magic_level_deque = deque(map(int, input().split()))


# Doll 150
# Wooden train 250
# Teddy bear 300
# Bicycle 400

toys_dict = {}

while True:
    if len(materials_stack) == 0 or len(magic_level_deque) == 0:
        break

    current_magic = materials_stack[-1] * magic_level_deque[0]
    print(current_magic)
    if current_magic in [150, 250, 300, 400]:
        if current_magic == 150:
            if 'Doll' not in toys_dict.keys():
                toys_dict['Doll'] = 0
            toys_dict['Doll'] += 1
        elif current_magic == 250:
            if 'Wooden train' not in toys_dict.keys():
                toys_dict['Wooden train'] = 0
            toys_dict['Wooden train'] += 1
        elif current_magic == 300:
            if 'Teddy bear' not in toys_dict.keys():
                toys_dict['Teddy bear'] = 0
            toys_dict['Teddy bear'] += 1
        elif current_magic == 400:
            if 'Bicycle' not in toys_dict.keys():
                toys_dict['Bicycle'] = 0
            toys_dict['Bicycle'] += 1

        materials_stack.pop()
        magic_level_deque.popleft()
    elif current_magic < 0:
        current_magic = materials_stack.pop() + magic_level_deque.popleft()
        materials_stack.append(current_magic)
    elif current_magic > 0:
        magic_level_deque.popleft()
        materials_stack[-1] += 15
    elif current_magic == 0:
        materials_stack.pop()
        magic_level_deque.popleft()
    print(materials_stack)
    print(magic_level_deque)

if ('Doll' in toys_dict.keys() and 'Wooden train' in toys_dict.keys()) or ('Teddy bear' in toys_dict.keys() and 'Bicycle' in toys_dict.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_stack:
    print(f"Materials left: {', '.join(map(str, materials_stack))}")

if magic_level_deque:
    print(f"Magic left: {', '.join(map(str, magic_level_deque))}")

for toy in sorted(toys_dict.keys()):
    print(f"{toy}: {toys_dict[toy]}")
'''

from collections import deque

toys = {
    'Doll': {
        'magic': 150,
        'crafted': 0
    },
    'Wooden train': {
        'magic': 250,
        'crafted': 0
    },
    'Teddy bear': {
        'magic': 300,
        'crafted': 0
    },
    'Bicycle': {
        'magic': 400,
        'crafted': 0
    }
}

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))
que = []

while materials and magic:
    total_magic_level = 0

    flag = False
    if materials[-1] == 0:
        materials.pop()
        flag = True

    if magic[0] == 0:
        magic.popleft()
        flag = True

    if flag:
        continue

    product = materials[-1] * magic[0]
    if product == toys['Doll']['magic']:
        toys['Doll']['crafted'] += 1
        materials.pop()
        magic.popleft()
    elif product == toys['Wooden train']['magic']:
        toys['Wooden train']['crafted'] += 1
        materials.pop()
        magic.popleft()
    elif product == toys['Teddy bear']['magic']:
        toys['Teddy bear']['crafted'] += 1
        materials.pop()
        magic.popleft()
    elif product == toys['Bicycle']['magic']:
        toys['Bicycle']['crafted'] += 1
        materials.pop()
        magic.popleft()
    else:
        if product > 0:
            materials[-1] += 15
            magic.popleft()
        elif product < 0:
            materials.append(materials.pop() + magic.popleft())


if (toys['Doll']['crafted'] > 0 and toys['Wooden train']['crafted'] > 0) or \
        (toys['Teddy bear']['crafted'] > 0 and toys['Bicycle']['crafted'] > 0):
    print('The presents are crafted! Merry Christmas!')
else:
    print("No presents this Christmas!")

if materials:
    for m in range(len(materials)):
        que.append(str(materials.pop()))
    print(f"Materials left: {', '.join(que)}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for toy in sorted(toys.keys()):
    if toys[toy]['crafted'] > 0:
        print(f"{toy}: {toys[toy]['crafted']}")