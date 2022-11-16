from collections import deque


def gift_check(gifts_dict, amount, material, magic_lvl):
    if 400 <= amount <= 499:
        gifts_dict['Diamond Jewellery'] += 1
        # material.pop()
        # magic_lvl.popleft()
    elif 300 <= amount <= 399:
        gifts_dict['Gold'] += 1
        # material.pop()
        # magic_lvl.popleft()
    elif 200 <= amount <= 299:
        gifts_dict['Porcelain Sculpture'] += 1
        # material.pop()
        # magic_lvl.popleft()
    elif 100 <= current_sum <= 199:
        gifts_dict['Gemstone'] += 1
        # material.pop()
        # magic_lvl.popleft()
    material.pop()
    magic_lvl.popleft()

    return gifts_dict


materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magic_level:
    current_sum = materials[-1] + magic_level[0]
    if current_sum >= 500:
        current_sum /= 2
        gifts = gift_check(gifts, current_sum, materials, magic_level)
    elif current_sum < 100:
        if current_sum % 2 == 0:
            materials[-1] = materials[-1] * 2
            magic_level[0] = magic_level[0] * 3
        else:
            current_sum = current_sum * 2
            gifts = gift_check(gifts, current_sum, materials, magic_level)
            # materials[-1] = materials[-1] * 2
            # magic_level[0] = magic_level[0] * 2
    else:  # less than 100
        gifts = gift_check(gifts, current_sum, materials, magic_level)

gifts = dict(sorted(gifts.items(), key=lambda x: x[0]))
if (gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0) or \
        (gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join(map(str, materials))}')
if magic_level:
    print(f'Magic left: {", ".join(map(str, magic_level))}')

for key, value in gifts.items():
    if value > 0:
        print(f"{key}: {value}")
