from collections import deque


def points_collect(r, c):
    current_points = 0
    current_points += int(board[0][c]) + int(board[-1][c]) + int(board[r][0]) + int(board[r][-1])

    return current_points


board_size = 7

first_player, second_player = input().split(', ')

players_status = deque([[first_player, 501], [second_player, 501]])
throws = {
    first_player: 0,
    second_player: 0
}

bullseye_hit = False

board = [input().split() for _ in range(board_size)]

while True:
    player, points = players_status[0][0], players_status[0][1]
    row, col = tuple(map(int, eval(input())))

    throws[player] += 1

    if not 0 <= row < board_size or not 0 <= col < board_size:
        players_status.append(players_status.popleft())
        continue

    if board[row][col].isdigit():
        points -= int(board[row][col])
    else:
        if board[row][col] == 'D':
            scored_points = points_collect(row, col)
            points -= scored_points * 2
        elif board[row][col] == 'T':
            scored_points = points_collect(row, col)
            points -= scored_points * 3
        elif board[row][col] == 'B':
            bullseye_hit = True

    if points <= 0 or bullseye_hit:
        print(f'{player} won the game with {throws[player]} throws!')
        break

    players_status[0][-1] = points
    players_status.append(players_status.popleft())


