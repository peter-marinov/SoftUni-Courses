age = int(input())
laundry_price = float(input())
toy_price = int(input())

toys = 0
money = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        money = money + 5 * i - 1# 2 - 10, 4 - 20, 6 - 30, 8 - 40
    else:
        toys += 1

# money_after_brother = money - age  # from brother
toys_money = toys * toy_price
total_money = money + toys_money

money_left = abs(total_money - laundry_price)
# print(money)
# print(money_after_brother)
# print(toys_money)
# print(total_money)
# print(money_left)

if total_money >= laundry_price:
    print(f"Yes! {money_left:.2f}")
else:
    print(f"No! {money_left:.2f}")