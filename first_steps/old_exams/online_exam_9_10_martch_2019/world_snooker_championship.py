tournament = input()
ticket_type = input()
tickets = int(input())
photo = input()

ticket_price = 0
total_price = 0
if tournament == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = tickets * 55.5
    elif ticket_type == "Premium":
        ticket_price = tickets * 105.2
    elif ticket_type == "VIP":
        ticket_price = tickets * 118.90
elif tournament == "Semi final":
    if ticket_type == "Standard":
        ticket_price = tickets * 75.88
    elif ticket_type == "Premium":
        ticket_price = tickets * 125.22
    elif ticket_type == "VIP":
        ticket_price = tickets * 300.4
elif tournament == "Final":
    if ticket_type == "Standard":
        ticket_price = tickets * 110.10
    elif ticket_type == "Premium":
        ticket_price = tickets * 160.66
    elif ticket_type == "VIP":
        ticket_price = tickets * 400

if ticket_price > 4000:
    total_price = ticket_price * 0.75
elif ticket_price > 2500:
    total_price = ticket_price * 0.9
    if photo == "Y":
        total_price += tickets * 40
else:
    total_price = ticket_price
    if photo == "Y":
        total_price += tickets * 40

print(f"{total_price:.2f}")