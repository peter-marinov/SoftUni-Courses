num = int(input())

sum_odd = 0
sum_even = 0
for i in range(1, num + 1): # защото ни трябват четни и нечетни позиции
    number_input = int(input())
    if i % 2 == 0:
        sum_even += number_input
    else:
        sum_odd += number_input

if sum_even == sum_odd:
    print(f"Yes\nSum = {sum_even}")
else:
    diff = abs(sum_even - sum_odd)
    print(f"No\nDiff = {diff}")