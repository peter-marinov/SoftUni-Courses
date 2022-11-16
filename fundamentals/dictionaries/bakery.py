food = input().split(' ')

bakery_dict = {food[i]: int(food[i + 1]) for i in range(0, len(food), 2)}

# for i in range(0, len(food), 2):
#     bakery_dict[food[i]] = int(food[i + 1])



print(bakery_dict)