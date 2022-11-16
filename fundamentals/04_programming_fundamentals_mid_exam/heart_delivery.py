def heart_delivery_func():
    pass

houses = list(map(int, input().split("@")))
current_house_index = 0
while True:
    command = input()
    if command == "Love!":
        print(f"Cupid's last position was {current_house_index}.")
        houses = [num for num in houses if num != 0]
        if len(houses):
            print(f"Cupid has failed {len(houses)} places.")
        else:
            print("Mission was successful.")
        break

    action, cupid_index = command.split(' ')
    cupid_index = int(cupid_index)
    if action == "Jump":
        if current_house_index + cupid_index <= len(houses) - 1:
            current_house_index += cupid_index
        else:
            # current_house_index = (current_house_index + cupid_index) - len(houses)
            current_house_index = 0
        for house in range(len(houses)):
            pass
        if houses[current_house_index] == 0:
            print(f"Place {current_house_index} already had Valentine's day.")
        else:
            houses[current_house_index] -= 2
            if houses[current_house_index] == 0:
                print(f"Place {current_house_index} has Valentine's day.")

