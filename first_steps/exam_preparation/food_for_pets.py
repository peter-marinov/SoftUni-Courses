days = int(input())
available_food = float(input())

biscuit_total = 0
total_food = 0
dog_total_food = 0
cat_total_food = 0
for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    daily_food = dog_food + cat_food
    if day % 3 == 0:
        biscuit_total = biscuit_total + (daily_food * 0.10)

    total_food = total_food + daily_food

    dog_total_food += dog_food
    cat_total_food += cat_food

percent_total = total_food / available_food * 100
percent_dog = dog_total_food / total_food * 100
percent_cat = cat_total_food / total_food * 100

print(f"Total eaten biscuits: {round(biscuit_total)}gr")
print(f"{percent_total:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")