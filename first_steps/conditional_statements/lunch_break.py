import math

serial = input()
serial_time = int(input())
break_time = int(input())

lunch_time = break_time * 1/8
rest_time = break_time * 0.25
break_time_left = break_time - lunch_time - rest_time

serial_time_left = math.ceil(abs(break_time_left - serial_time))

if serial_time <= break_time_left:
    print(f'You have enough time to watch {serial} and left with {serial_time_left} minutes free time.')
else:
    print(f"You don't have enough time to watch {serial}, you need {serial_time_left} more minutes.")

