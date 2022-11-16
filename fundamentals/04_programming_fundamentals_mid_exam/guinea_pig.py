quantity_of_food = float(input())
quantity_of_hay = float(input())
quantity_of_cover = float(input())
weight = float(input())

food_is_enough = True
for day in range(1, 31):
    quantity_of_food -= 0.3
    if day % 2 == 0:
        quantity_of_hay -= quantity_of_food * 0.05
    if day % 3 == 0:
        quantity_of_cover -= weight * 1/3

    if quantity_of_food < 0 or quantity_of_hay < 0 or quantity_of_cover <0:
        food_is_enough = False

if food_is_enough:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food:.2f}, Hay: {quantity_of_hay:.2f}, Cover: {quantity_of_cover:.2f}.")
else:
    print("Merry must go to the pet store!")

# a month is 30 days