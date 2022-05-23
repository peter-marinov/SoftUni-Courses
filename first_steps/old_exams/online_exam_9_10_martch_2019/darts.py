player_name = input()

starting_points = 301
hit_points = 0
game_is_won = False
successful_shots_count = 0
unsuccessful_shots_count = 0

while game_is_won == False:
    command = input()
    if command == "Retire":
        break
    points = int(input())
    if command == "Single":
        hit_points = points
    elif command == "Double":
        hit_points = points * 2
    elif command == "Triple":
        hit_points = points * 3

    if hit_points > starting_points:
        unsuccessful_shots_count += 1
        continue
    else:
        successful_shots_count += 1
        starting_points -= hit_points
        if starting_points == 0:
            game_is_won = True
            break


if game_is_won:
    print(f"{player_name} won the leg with {successful_shots_count} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_shots_count} unsuccessful shots.")