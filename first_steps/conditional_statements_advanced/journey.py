budget = float(input())
season = input()

money_spent = 0
location = ""
type_of_hotel = ""

if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        money_spent = budget * 0.30
    else:
        money_spent = budget * 0.70
elif budget <= 1000:
    location = "Balkans"
    if season == "summer":
        money_spent = budget * 0.40
    else:
        money_spent = budget * 0.80
else:
    location = "Europe"
    money_spent = budget * 0.90

if location == "Europe":
    type_of_hotel = "Hotel"
else:
    if season == "summer":
        type_of_hotel = "Camp"
    else: # winter
        type_of_hotel = "Hotel"

print(f"Somewhere in {location}")
print(f"{type_of_hotel} - {money_spent:.2f}")