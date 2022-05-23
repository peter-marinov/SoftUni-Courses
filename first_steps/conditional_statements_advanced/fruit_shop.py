fruit = input()
day = input()
volume = float(input())

is_working_day = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' \
    or day == 'Friday'
is_weekend = day == 'Sunday' or day == 'Saturday'
valid = True

if is_working_day:
    if fruit == 'banana':
        price = volume * 2.50
    elif fruit == 'apple':
        price = volume * 1.20
    elif fruit == 'orange':
        price = volume * 0.85
    elif fruit == 'grapefruit':
        price = volume * 1.45
    elif fruit == 'kiwi':
        price = volume * 2.70
    elif fruit == 'pineapple':
        price = volume * 5.50
    elif fruit == 'grapes':
        price = volume * 3.85
    else:
        valid = False
elif is_weekend:
    if fruit == 'banana':
        price = volume * 2.70
    elif fruit == 'apple':
        price = volume * 1.25
    elif fruit == 'orange':
        price = volume * 0.90
    elif fruit == 'grapefruit':
        price = volume * 1.60
    elif fruit == 'kiwi':
        price = volume * 3.00
    elif fruit == 'pineapple':
        price = volume * 5.60
    elif fruit == 'grapes':
        price = volume * 4.20
    else:
        valid = False
else:
    valid = False

if valid:
    print(f'{price:.2f}')
else:
    print('error')