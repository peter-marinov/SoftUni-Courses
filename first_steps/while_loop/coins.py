current_sum = float(input())

current_sum = int(current_sum * 100)
coins_count = 0

# 200 -> 2lv
# 100 -> 1lv

coins_count += current_sum // 200
current_sum %= 200
print(coins_count)
print(current_sum)
coins_count += current_sum // 100
current_sum %= 100
print(coins_count)
print(current_sum)
coins_count += current_sum // 50
current_sum %= 50
print(coins_count)
print(current_sum)
coins_count += current_sum // 20
current_sum %= 20
print(coins_count)
print(current_sum)
coins_count += current_sum // 10
current_sum %= 10
print(coins_count)
print(current_sum)
coins_count += current_sum // 5
current_sum %= 5
print(coins_count)
print(current_sum)
coins_count += current_sum // 2
current_sum %= 2
print(coins_count)
print(current_sum)
coins_count += current_sum // 1
current_sum %= 1
print(coins_count)
print(current_sum)

print(coins_count)
