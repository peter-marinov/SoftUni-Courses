day = input()

price = 0
if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
    price = 12
elif day == 'Wednesday' or day == 'Thursday':
    price = 14
elif day == 'Saturday' or day == 'Sunday':
    price = 16

print(price)