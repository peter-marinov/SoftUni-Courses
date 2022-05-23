import math

tournaments = int(input())
starting_points = int(input())

win = 0
finalist = 0
semifinalist = 0
tournaments_points = 0
for i in range(1, tournaments + 1):
    result = input()
    if result == "W":
        win += 1
    elif result == "F":
        finalist += 1
    elif result == "SF":
        semifinalist += 1

# print(f"{win} {finalist} {semifinalist}")
tournaments_points = win * 2000 + finalist * 1200 + semifinalist * 720
# print(tournaments_points)
avarage_points = math.floor(tournaments_points / tournaments)
wins_percent = win / tournaments * 100
final_points = starting_points + tournaments_points

print(f"Final points: {final_points}")
print(f"Average points: {avarage_points}")
print(f"{wins_percent:.2f}%")
