from collections import deque


def place_circle(row):
    if row == rows - 1 or board[row + 1][player_col] != empty_cell_symbol:
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


player_one_symbol = input("Player one, select your game symbol: ")
while True:
    player_two_symbol = input("Player two, select your game symbol: ")
    if player_one_symbol == player_two_symbol:
        print('Symbol is already taken by player one.')
    else:
        break

rows, cols = 6, 7

empty_cell_symbol = '-'
turn = deque([[1, player_one_symbol], [2, player_two_symbol]]) # turn.append(turn.pop(0))
board = [[empty_cell_symbol] * cols for row in range(rows)]

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

numbers = [i for i in range(1, cols + 1)]

while not win:
    [print(f"[ {'  '.join(row)} ]") for row in board]
    print('‾' * 23)
    print(f"[ {'  '.join(map(str, numbers))} ]")

    player_number, player_symbol = turn[0]

    try:
        player_col = int(input(f"\nPlayer {player_number}, please choose a column: ")) - 1
    except ValueError:
        print("Please select a number")
        continue

    if not 0 <= player_col < cols:
        print(f"Select a valid number between 1 and {cols}")
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