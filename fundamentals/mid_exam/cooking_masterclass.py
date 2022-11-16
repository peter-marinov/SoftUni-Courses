from math import ceil

budget = float(input())
students = int(input())
price_of_flour = float(input())
price_of_egg = float(input())
price_of_apron = float(input())

calculated_price = 0

#One student = 1 package of flour, 10 eggs and an apron

price_for_all_flour = (students - (students // 5)) * price_of_flour
# print(students * 10 // 5)
price_for_all_eggs = students * price_of_egg * 10
price_for_all_apron = price_of_apron * ceil(students * 1.2)

# print(price_for_all_flour, price_for_all_eggs, price_for_all_apron)

calculated_price = price_for_all_flour + price_for_all_eggs + price_for_all_apron
if calculated_price <= budget:
    print(f"Items purchased for {calculated_price:.2f}$.")
else:
    needed_money = abs(calculated_price - budget)
    print(f"{needed_money:.2f}$ more needed.")