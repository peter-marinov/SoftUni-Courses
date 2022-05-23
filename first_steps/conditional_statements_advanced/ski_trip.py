days = int(input())
type_of_stay = input()
feedback = input()

nights = days - 1
final_price = 0

if type_of_stay == "room for one person":
    final_price = nights * 18
    # if nights < 10:
    #     final_price = nights * 18
    # elif nights <=15:
    #     final_price = nights * 18
    # else:
    #     final_price = nights * 18
elif type_of_stay == "apartment":
    if nights < 10:
        final_price = nights * 25 * 0.7
    elif nights <= 15:
        final_price = nights * 25 * 0.65
    else:
        final_price = nights * 25 * 0.5
elif type_of_stay == "president apartment":
    if nights < 10:
        final_price = nights * 35 * 0.9
    elif nights <= 15:
        final_price = nights * 35 * 0.85
    else:
        final_price = nights * 35 * 0.8

if feedback == "positive":
    final_price *= 1.25
else:
    final_price *= 0.9

print(f"{final_price:.2f}")