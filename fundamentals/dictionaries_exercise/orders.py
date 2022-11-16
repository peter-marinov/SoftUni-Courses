def items_set (bill_dict, item_name, item_price, volume):
    if item_name not in bill_dict.keys():
        bill_dict[item_name] = [item_price, volume]
    else:
        bill_dict[item_name][0] = item_price
        bill_dict[item_name][1] += volume
    return bill_dict


def print_prices_per_item(bill_dict):
    for current_item in bill_dict.keys():
        current_item_price = bill_dict[current_item][0] * bill_dict[current_item][1]
        print(f'{current_item} -> {current_item_price:.2f}')

orders_dict = {}

while True:
    command = input().split(' ')
    if command[0] == "buy":
        break

    item, price, quantity = command[0], float(command[1]), int(command[2])
    orders_dict = items_set(orders_dict, item, price, quantity)

print_prices_per_item(orders_dict)
