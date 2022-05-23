# is_even = False
# number = 1
# if number % 2 == 0:
#     is_even = True
# print(is_even)
# number += 1
# if number % 2 == 0:
#     is_even = True
# print(is_even)

type_of_the_movie = input()
rows = int(input())
columns = int(input())

total_places = rows * columns
price_per_ticket = 0

if type_of_the_movie == "Premiere":
    price_per_ticket = 12
elif type_of_the_movie == "Normal":
    price_per_ticket = 7.50
elif type_of_the_movie == "Discount":
    price_per_ticket = 5

total_income = total_places * price_per_ticket
print(f"{total_income:.2f} leva")