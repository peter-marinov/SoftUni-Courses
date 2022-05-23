month = input()
nights_number = int(input())

apartments_price = 0
studios_price = 0

if month == "May" or month == "October":
    apartments_price = nights_number * 65
    studios_price = nights_number * 50
    # if 14 > nights_number > 7:
    #     studios_price *= 0.95
    # else: # when it is more than 14 nights
    #     studios_price *= 0.7
    #     apartments_price *= 0.9
    if nights_number > 14:
        studios_price *= 0.7
        apartments_price *= 0.9
    elif nights_number > 7:
        studios_price *= 0.95
elif month == "June" or month == "September":
    apartments_price = nights_number * 68.70
    studios_price = nights_number * 75.20
    if nights_number > 14:
        studios_price *= 0.80
        apartments_price *= 0.9
elif month == "July" or month == "August":
    apartments_price = nights_number * 77
    studios_price = nights_number * 76
    if nights_number > 14:
        apartments_price *= 0.9

print(f"Apartment: {apartments_price:.2f} lv.")
print(f"Studio: {studios_price:.2f} lv.")

# Да се отпечатат на конзолата 2 реда:
#  На първия ред: Apartment: {цена за целият престой} lv.
#  На втория ред:Studio: {цена за целият престой} lv.
# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.