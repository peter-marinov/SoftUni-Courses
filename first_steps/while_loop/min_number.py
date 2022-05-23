import sys

command = input()
min_number = sys.maxsize
while command != "Stop":
    current_num = int(command)
    if min_number > current_num:
        min_number = current_num

    command = input()

print(min_number)
