numbers = input().split(' ')

abs_numbers = []
for num in numbers:
    abs_numbers.append(abs(float(num)))

print(abs_numbers)

# numbers = list(map(float, input().split(' ')))
# results = []

# def abs_numbers(nums):
#     results = [abs(num) for num in nums]
#     return results

