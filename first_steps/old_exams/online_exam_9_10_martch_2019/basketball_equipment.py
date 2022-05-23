year_tax = int(input())
shoes_price = year_tax * 0.6
kit_price = shoes_price * 0.8
ball_price = kit_price * 0.25
accessories_price = ball_price * 0.2

total_price = year_tax + shoes_price + kit_price + ball_price + accessories_price
print(f"{total_price:.2f}")