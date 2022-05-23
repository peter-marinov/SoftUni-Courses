mins_walk_daily = int(input())
walks_daily = int(input())
calories = int(input())

walks_time = mins_walk_daily * walks_daily
burned_calories = walks_time * 5

if calories * 0.5 <= burned_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.')