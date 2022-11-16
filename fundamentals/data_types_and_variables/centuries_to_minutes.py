number_of_centuries = int(input())

years = number_of_centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{number_of_centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')