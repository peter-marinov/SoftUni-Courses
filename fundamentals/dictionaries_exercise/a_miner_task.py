miner_dict = {}

while True:
    resource = input()
    if resource == 'stop':
        break

    quantity = int(input())
    if resource in miner_dict:
        miner_dict[resource] += quantity
    else:
        miner_dict[resource] = quantity

output_print = [f'{resource} -> {quantity}' for resource, quantity in miner_dict.items()]
print('\n'.join(output_print))
# print(miner_dict)