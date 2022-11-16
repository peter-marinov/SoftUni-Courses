def add_initial_pieces(number_of_pieces):
    initial_pieces_dict = {}
    for _ in range(number_of_pieces):
        piece, composer, key = input().split("|")
        initial_pieces_dict[piece] = [composer, key]
    return initial_pieces_dict


def edit_pieces_dict(pieces_dict, command):
    action = command[0]
    if action == "Add":
        piece, composer, key = command[1:]
        if piece in pieces_dict.keys():
            print(f"{piece} is already in the collection!")
        else:
            pieces_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        piece = command[1]
        if piece in pieces_dict.keys():
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        piece, new_key = command[1:]
        if piece in pieces_dict.keys():
            pieces_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    return pieces_dict

number_of_pieces = int(input())

pieces_dict = add_initial_pieces(number_of_pieces)

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break
    pieces_dict = edit_pieces_dict(pieces_dict, command)

for piece in pieces_dict.keys():
    print(f"{piece} -> Composer: {pieces_dict[piece][0]}, Key: {pieces_dict[piece][1]}")