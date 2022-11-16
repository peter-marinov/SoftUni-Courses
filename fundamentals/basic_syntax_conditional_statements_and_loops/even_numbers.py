iterations = int(input())

is_even = True
for number in range(0, iterations):
    user_number = int(input())
    if user_number % 2 != 0:
        is_even = False
        print(f'{user_number} is odd!')
        break

if is_even:
    print('All numbers are even.')