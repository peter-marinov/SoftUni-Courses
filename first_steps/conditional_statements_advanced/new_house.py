flower_type = input()
flower_number = int(input())
budget = int(input())

flowers_price = 0

if flower_type == "Roses":
    if flower_number > 80:
        flowers_price = flower_number * 5 * 0.9
    else:
        flowers_price = flower_number * 5
elif flower_type == "Dahlias":
    if flower_number > 90:
        flowers_price = flower_number * 3.80 * 0.85
    else:
        flowers_price = flower_number * 3.80
elif flower_type == "Tulips":
    if flower_number > 80:
        flowers_price = flower_number * 2.80 * 0.85
    else:
        flowers_price = flower_number * 2.80
elif flower_type == "Narcissus":
    if flower_number < 120:
        flowers_price = flower_number * 3.00 * 1.15
    else:
        flowers_price = flower_number * 3.00
elif flower_type == "Gladiolus":
    if flower_number < 80:
        flowers_price = flower_number * 2.50 * 1.20
    else:
        flowers_price = flower_number * 2.50

money_left = abs(budget - flowers_price)

if budget >= flowers_price:
    print(f"Hey, you have a great garden with {flower_number} {flower_type} and \
{money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left:.2f} leva more.")