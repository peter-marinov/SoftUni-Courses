pages = int(input())
pages_per_hour = int(input())
days = int(input())

needed_hours = pages // (pages_per_hour * days)

print(needed_hours)
