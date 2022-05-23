hours = int(input())
minutes = int(input())

if minutes + 15 >= 60:
    new_minutes = minutes + 15 - 60
    new_hours = hours + 1
else:
    new_minutes = minutes + 15
    new_hours = hours

if new_hours > 23:
    new_hours = 0

print(f'{new_hours}:{new_minutes:02d}')