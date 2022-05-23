import math

tennis_rocket_price = float(input())
number_of_tennis_rockets = int(input())
number_of_shoes = int(input())

total_tennis_rocket_price = tennis_rocket_price * number_of_tennis_rockets
shoe_price = tennis_rocket_price * 1 / 6
total_shoe_price = number_of_shoes * shoe_price

all_price = (total_shoe_price + total_tennis_rocket_price) * 1.2

djokovic_part = math.floor(all_price / 8)
sponsors_part = math.ceil(all_price * 7 / 8)

print(f"Price to be paid by Djokovic {djokovic_part}")
print(f"Price to be paid by sponsors {sponsors_part}")


