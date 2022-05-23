daily_money = float(input())
money_from_sales = float(input())
spend_money = float(input())
gift_price = float(input())

total_money_from_sales = 0
# for day in range(1, 5+1):
total_money_from_sales = money_from_sales * 5
# print(total_money_from_sales)
total_daily_money = daily_money * 5
# print(total_daily_money)
total_left_money = total_daily_money + total_money_from_sales - spend_money
# print(total_left_money)

if total_left_money >= gift_price:
    print(f"Profit: {total_left_money:.2f} BGN, the gift has been purchased.")
else:
    diff = abs(total_left_money - gift_price)
    print(f"Insufficient money: {diff:.2f} BGN.")

