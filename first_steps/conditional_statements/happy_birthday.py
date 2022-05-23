rent = float(input())

cake_price = rent * 0.2
drinks_price = cake_price * 0.55
palqk_price = rent * 1/3

# print(f'{cake_price} {drinks_price} {palqk_price}')

needed_budget = rent + cake_price + drinks_price + palqk_price
print(needed_budget)