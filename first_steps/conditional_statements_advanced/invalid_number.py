num = int(input())

valid = (num >= 100 and num <= 200) or num == 0

if not valid:
    print('invalid')