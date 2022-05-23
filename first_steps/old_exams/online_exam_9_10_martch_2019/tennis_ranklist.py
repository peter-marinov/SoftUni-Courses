import math

tournaments = int(input())
starting_points = int(input())

tournaments_points = 0
won_tournaments = 0
for i in range(1, tournaments + 1):
    result = input()
    if result == "W":
        tournaments_points += 2000
        won_tournaments += 1
    elif result == "F":
        tournaments_points += 1200
    elif result == "SF":
        tournaments_points += 720

final_points = starting_points + tournaments_points
average_points = math.floor(tournaments_points / tournaments)
percent_won_tournaments = won_tournaments / tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_won_tournaments:.2f}%")