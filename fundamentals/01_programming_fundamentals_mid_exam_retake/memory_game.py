elements = input().split(" ")
turns = 0

while True:
    # print(elements)
    guess = input()
    if guess == "end":
        print(f"Sorry you lose :(")
        print(" ".join(elements))
        break
    turns += 1
    first_index, second_index = list(map(int, guess.split()))
    if first_index == second_index or \
            first_index < 0 or second_index < 0 or \
            first_index > len(elements) - 1 or second_index > len(elements) -1 :
        elements.insert((int(len(elements) / 2)), "-"+str(turns)+"a")
        elements.insert((int(len(elements) / 2)) + 1, "-"+str(turns)+"a")
        item_to_insert = "-"+str(turns)+"a"

        print("Invalid input! Adding additional elements to the board")
        continue
    if elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        elements[first_index], elements[second_index] = "remove_key", "remove_key"
        elements.remove("remove_key")
        elements.remove("remove_key")
    elif elements[first_index] != elements[second_index]:
        print("Try again!")

    if not elements:
        print(f"You have won in {turns} turns!")
        break
