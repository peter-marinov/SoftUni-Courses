people_in_group = int(input())
nights = int(input())
transport_cards = int(input())
museum_cards = int(input())

nights_price = nights * 20
transport_cards_price = transport_cards * 1.60
museum_cards_price = museum_cards * 6
price_for_one = nights_price + transport_cards_price + museum_cards_price
total_price = price_for_one * people_in_group * 1.25
print(f"{total_price:.2f}")
