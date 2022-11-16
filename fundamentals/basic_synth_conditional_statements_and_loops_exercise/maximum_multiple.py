divisor = int(input())
boundary = int(input())

max_multiplier = 0
for current_number in range(boundary, divisor, -1):
    if current_number % divisor == 0:
        max_multiplier = current_number
        break

print(max_multiplier)

