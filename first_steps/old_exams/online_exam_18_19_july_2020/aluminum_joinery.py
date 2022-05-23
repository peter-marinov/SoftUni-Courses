number_of_windows = int(input())
window_size = input()
way_of_delivery = input()

# total_price = 0
unit_price = 0
is_possible_to_create = True
if number_of_windows < 10:
    is_possible_to_create = False
    print("Invalid order")
    exit()
if window_size == "90X130":
    if number_of_windows <= 30:
        unit_price = 110
    elif number_of_windows > 60:
        unit_price = 110 * 0.92
    else:
        unit_price = 110 * 0.95
elif window_size == "100X150":
    if number_of_windows <= 40:
        unit_price = 140
    elif number_of_windows > 80:
        unit_price = 140 * 0.9
    else:
        unit_price = 140 * 0.94
elif window_size == "130X180":
    if number_of_windows <= 20:
        unit_price = 190
    elif number_of_windows > 50:
        unit_price = 190 * 0.88
    else:
        unit_price = 190 * 0.93
elif window_size == "200X300":
    if number_of_windows <= 25:
        unit_price = 250
    elif number_of_windows > 50:
        unit_price = 250 * 0.86
    else:
        unit_price = 250 * 0.91

total_price = unit_price * number_of_windows
if number_of_windows > 99:
    if way_of_delivery == "With delivery":
        final_price = (total_price + 60) * 0.96
    else:
        final_price = total_price * 0.96
else:
    if way_of_delivery == "With delivery":
        final_price = total_price + 60
    else:
        final_price = total_price

print(f"{final_price:.2f} BGN")


