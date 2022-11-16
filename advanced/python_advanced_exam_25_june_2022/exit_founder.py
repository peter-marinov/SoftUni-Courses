def move(maze, row, col, player):
    game_finished = False
    skip_move = False
    if maze[row][col] == exit:
        print(f"{player} found the Exit and wins the game!")
        game_finished = True
        return game_finished, skip_move
    elif maze[row][col] == trap:
        "{player} is out of the game! The winner is {winner}."
    elif maze[row][col] == wall:
        pass
    elif maze[row][col] == empty:
        pass


size = 6

first_player, second_player = input().split(', ')
matrix = [input().split(' ') for _ in range(size)]
first_player_ignored = False
second_player_ignored = False
exit = "E"
trap = "T"
wall = "W"
empty = '.'

while True:
    first_row, first_col = tuple(map(int, input()[1:-1].split(', ')))
    if not first_player_ignored:
        if matrix[first_row][first_col] == exit:
            print(f"{first_player} found the Exit and wins the game!")
            break
        elif matrix[first_row][first_col] == trap:
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        elif matrix[first_row][first_col] == wall:
            print(f"{first_player} hits a wall and needs to rest.")
            first_player_ignored = True
    else:
        first_player_ignored = False

    second_row, second_col = tuple(map(int, input()[1:-1].split(', ')))
    if not second_player_ignored:
        if matrix[second_row][second_col] == exit:
            print(f"{second_player} found the Exit and wins the game!")
            break
        elif matrix[second_row][second_col] == trap:
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        elif matrix[second_row][second_col] == wall:
            print(f"{second_player} hits a wall and needs to rest.")
            second_player_ignored = True
    else:
        second_player_ignored = False
