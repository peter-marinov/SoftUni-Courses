air_company = input()
regular_people_tickets = int(input())
kids_tickets = int(input())
regular_people_price = float(input())
tax_per_ticket = float(input())

regular_people_total_price = (regular_people_price + tax_per_ticket) * regular_people_tickets
kids_price = regular_people_price * 0.3
kids_total_price = (kids_price + tax_per_ticket) * kids_tickets
# total_price = kids_total_price + regular_people_total_price
# print(total_price)
profit = (kids_total_price + regular_people_total_price) * 0.2

print(f"The profit of your agency from {air_company} tickets is {profit:.2f} lv.")