number_of_liters = int(input())
water_capacity = 255

current_water = 0
for water in range(number_of_liters):
    added_water = int(input())
    current_water += added_water
    if current_water > water_capacity:
        print('Insufficient capacity!')
        current_water -= added_water

print(current_water)
# if water_capacity >= current_water:
#     print(water_capacity - current_water)

