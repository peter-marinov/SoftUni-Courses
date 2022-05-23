budget = float(input())
people = int(input())
clothe_price = float(input())

if people > 150:
    clothes_price = clothe_price * people * 0.9
else:
    clothes_price = clothe_price * people

decor_price = budget * 0.1

abs_money = abs(budget - (decor_price + clothes_price))

if (decor_price + clothes_price > budget):
    print('Not enough money!')
    print(f'Wingard needs {abs_money:.02f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {abs_money:.02f} leva left.')