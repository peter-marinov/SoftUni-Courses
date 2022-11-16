input_value = int(input())
# from nltk.chat.util import Chat, reflections
# digit_sum = 0
for num in range(1, input_value+1):
    sum_of_digits = 0
    digits = num

    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
