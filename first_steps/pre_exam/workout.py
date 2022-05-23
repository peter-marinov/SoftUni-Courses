import math

number_of_days = int(input())
first_day_km = float(input())

needed_distance = 1000
current_km = first_day_km
total_ran_km = first_day_km
for day in range(1, number_of_days+1):
    # print(current_km)
    percent_improvement = int(input())
    current_km = current_km * (1 + (percent_improvement / 100))
    total_ran_km += current_km

# print(total_ran_km)
diff = math.ceil(abs(total_ran_km - needed_distance))
if total_ran_km >= needed_distance:
    print(f"You've done a great job running {diff} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers")