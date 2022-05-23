price_above_20_kg = float(input())
weigh_of_luggage = float(input())
days_until_journey = int(input())
number_of_luggage = int(input())

total_price = 0
price_per_luggage = 0
if weigh_of_luggage < 10:
    price_per_luggage = price_above_20_kg * 0.2
elif weigh_of_luggage > 20:
    price_per_luggage = price_above_20_kg
else: # between [10 and 20]
    price_per_luggage = price_above_20_kg * 0.5

if days_until_journey < 7:
    price_per_luggage *= 1.4
elif days_until_journey > 30:
    price_per_luggage *= 1.1
else: # between [7 and 30]
    price_per_luggage *= 1.15

total_price = price_per_luggage * number_of_luggage
print(f"The total price of bags is: {total_price:.2f} lv.")