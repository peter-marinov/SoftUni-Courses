tournament_name = input()

won_games = 0
lost_games = 0
played_games = 0
while tournament_name != "End of tournaments":
    number_of_games = int(input())
    for game in range(1, number_of_games + 1):
        desi_team_points = int(input())
        other_team_points = int(input())

        played_games += 1

        diff = abs(desi_team_points - other_team_points)
        if desi_team_points > other_team_points:
            won_games += 1
            print(f"Game {game} of tournament {tournament_name}: win with {diff} points.")
        elif desi_team_points < other_team_points:
            lost_games += 1
            print(f"Game {game} of tournament {tournament_name}: lost with {diff} points.")

    tournament_name = input()

# print(won_games)
# print(lost_games)
percent_won_games = won_games / played_games * 100
percent_lost_games = lost_games / played_games * 100
print(f"{percent_won_games:.2f}% matches win")
print(f"{percent_lost_games:.2f}% matches lost")