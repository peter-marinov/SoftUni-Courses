trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_price = puzzles * 2.60
dolls_price = dolls * 3.00
bears_price = bears * 4.10
minions_price = minions * 8.20
trucks_price = trucks * 2.00

toys_number = puzzles + dolls + bears + minions + trucks

toys_price = puzzles_price + dolls_price + bears_price + minions_price + trucks_price
if toys_number >= 50:
    toys_price = toys_price * 0.75

money_left = toys_price * 0.9 # after the rent
gold = abs(money_left - trip_price)
print(gold)
if money_left < trip_price:
    print(f'Not enough money! {trip_price - money_left:.02f} lv needed.')
else:
    print(f'Yes! {money_left - trip_price:.02f} lv left.')

# print('Not enough money! 238.73 lv needed.')