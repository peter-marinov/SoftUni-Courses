budget = float(input())
video_cards = int(input())
cpu = int(input())
ram = int(input())

video_cards_price = video_cards * 250
cpu_price = cpu * video_cards_price * 0.35
ram_price = ram * video_cards_price * 0.10
total_price = video_cards_price + cpu_price + ram_price

if video_cards > cpu:
    total_price *= 0.85


money_left = abs(budget - total_price)

if total_price <= budget:
    print(f'You have {money_left:.2f} leva left!')
else:
    print(f'Not enough money! You need {money_left:.2f} leva more!')