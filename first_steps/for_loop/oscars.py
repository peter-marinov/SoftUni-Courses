actor = input()
points_from_academy = float(input())
jury = int(input())

total_jury_points = 0
total_points = 0
for i in range(1, jury + 1):
    jury_name = input()
    jury_points = float(input())
    letters = len(jury_name)
    total_jury_points += letters * jury_points / 2
    total_points = points_from_academy + total_jury_points
    if total_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points <= 1250.5:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor} you need {needed_points:.1f} more!")



