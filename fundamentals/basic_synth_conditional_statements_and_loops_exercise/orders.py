number_of_orders = int(input())

total_price = 0

for order in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    amount_of_capsule = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif amount_of_capsule < 1 or amount_of_capsule > 2000:
        continue

    current_price = capsule_price * days * amount_of_capsule
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")


print(f"Total: ${total_price:.2f}")