wins = 0
draws = 0
loses = 0

for games in range(1, 3 + 1):
    game_result = input()
    home_team_goals = 0
    away_team_goals = 0
    count_string = 0
    result = game_result.split(":")
    if result[0] > result[1]:
        wins += 1
    elif result[0] == result[1]:
        draws += 1
    elif result[0] < result[1]:
        loses += 1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")