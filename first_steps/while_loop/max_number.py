import sys

command = input()
max_number = -sys.maxsize
while command != "Stop":
    current_num = int(command)
    if max_number < current_num:
        max_number = current_num

    command = input()

print(max_number)
