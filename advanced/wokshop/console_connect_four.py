from collections import deque


def place_circle(row):
    if row == rows - 1 or board[row + 1][player_col] != "0":
        board[row][player_col] = player_symbol
        return

    place_circle(row + 1)


def check_for_win(r, c, coordinates, iterations):
    if not (0 <= r < rows and 0 <= c < cols):
        return False

    if board[r][c] != player_symbol:
        return False

    if iterations == 3:
        [print(f"[ {', '.join(row)} ]") for row in board]
        print(f"The winner is player: {player_number}")
        return True

    return check_for_win(r + coordinates[0], c + coordinates[1], coordinates, iterations + 1)


player_one_symbol = "1"
player_two_symbol = "2"

rows, cols = 6, 7

turn = deque([[1, player_one_symbol], [2, player_two_symbol]])
board = [["0"] * cols for row in range(rows)]

win = False

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1),
)

while not win:
    [print(f"[ {', '.join(row)} ]") for row in board]

    player_number, player_symbol = turn[0]

    try:
        player_col = int(input(f"\nPlayer {player_number}, please choose a column: ")) - 1
    except ValueError:
        print("Select a valid number")
        continue

    if not 0 <= player_col < cols:
        print(f"Select a valid number in the range ({1} {cols})")
        continue

    row = 0

    if board[row][player_col] != "0":
        print("No empty spaces on that row!")

    place_circle(row)

    for row in range(rows):
        for col in range(cols):
            if board[row][col] != player_symbol:
                continue

            for coordinates in directions:
                win = check_for_win(row + coordinates[0], col + coordinates[1], coordinates, 1)

                if win:
                    break

            if win:
                break

        if win:
            break

    turn.append(turn.popleft())