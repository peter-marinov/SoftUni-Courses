days_in_hotel = int(input())
room_type = input()
score = input()

nights_in_hotel = days_in_hotel - 1
room_for_one_person_price = 18.00
apartment_price = 25.00
president_apartment_price = 35.00
total_nights_price = 0
if nights_in_hotel < 10:
    if room_type == "room for one person":
        total_nights_price = nights_in_hotel * room_for_one_person_price
    elif room_type == "apartment":
        total_nights_price = nights_in_hotel * apartment_price * 0.7
    elif room_type == "president apartment":
        total_nights_price = nights_in_hotel * president_apartment_price * 0.9
elif nights_in_hotel > 15:
    if room_type == "room for one person":
        total_nights_price = nights_in_hotel * room_for_one_person_price
    elif room_type == "apartment":
        total_nights_price = nights_in_hotel * apartment_price * 0.5
    elif room_type == "president apartment":
        total_nights_price = nights_in_hotel * president_apartment_price * 0.8
else:   # between [10 and 15]
    if room_type == "room for one person":
        total_nights_price = nights_in_hotel * room_for_one_person_price
    elif room_type == "apartment":
        total_nights_price = nights_in_hotel * apartment_price * 0.65
    elif room_type == "president apartment":
        total_nights_price = nights_in_hotel * president_apartment_price * 0.85

if score == "positive":
    total_nights_price = total_nights_price * 1.25
else:
    total_nights_price = total_nights_price * 0.9

print(f"{total_nights_price:.2f}")