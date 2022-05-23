first_player = input()
second_player = input()

# command = input()
first_player_card = input()
second_player_card = input()
first_player_points = 0
second_player_points = 0
is_number_wars = False
winner_name = ""
winner_points = 0
while first_player_card != "End of game" or second_player_card != "End of game":
    first_player_card_as_int = int(first_player_card)
    second_player_card_as_int = int(second_player_card)
    if first_player_card_as_int > second_player_card_as_int:
        first_player_points = first_player_points + first_player_card_as_int - second_player_card_as_int
    elif first_player_card_as_int < second_player_card_as_int:
        second_player_points = second_player_points + second_player_card_as_int - first_player_card_as_int
    elif first_player_card_as_int == second_player_card_as_int:
        first_player_card = input()
        second_player_card = input()
        first_player_card_as_int = int(first_player_card)
        second_player_card_as_int = int(second_player_card)

        if first_player_card_as_int > second_player_card_as_int:
            winner_name = first_player
            winner_points = first_player_points
        elif first_player_card_as_int < second_player_card_as_int:
            winner_name = second_player
            winner_points = second_player_points
        is_number_wars = True
        break

    first_player_card = input()
    if first_player_card == "End of game":
        break
    second_player_card = input()
    if second_player_card == "End of game":
        break


if is_number_wars:
    print("Number wars!")
    print(f"{winner_name} is winner with {winner_points} points")
else:
    print(f"{first_player} has {first_player_points} points")
    print(f"{second_player} has {second_player_points} points")
