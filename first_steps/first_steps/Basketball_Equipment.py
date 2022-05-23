annual_tax = int(input())
sneaker_price = annual_tax - (annual_tax * 40 / 100)
dress_price = sneaker_price - (sneaker_price * 20 / 100)
ball_price = dress_price * 0.25
other_price = ball_price * 0.20
final_sum = annual_tax + sneaker_price + dress_price + ball_price + other_price
print(final_sum)

