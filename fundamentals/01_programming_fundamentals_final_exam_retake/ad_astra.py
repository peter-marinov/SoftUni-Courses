import re

data = input()

search_pattern = r'([#|])([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'

result = re.findall(search_pattern, data)

total_calories = sum([int(calorie[3]) for calorie in result])
number_of_days = total_calories // 2000

print(f"You have food to last you for: {number_of_days} days!")
for food in result:
    print(f"Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[3]}")
