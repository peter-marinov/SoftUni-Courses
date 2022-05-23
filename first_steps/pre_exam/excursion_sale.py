number_of_sea_trips = int(input())
number_of_mountain_trips = int(input())

command = input()
sea_is_sold = False
mountain_is_sold = False
sea_trips_count = 0
mountain_trips_count = 0
while command != "Stop":
    if command == "sea":
        if sea_trips_count < number_of_sea_trips:
            sea_trips_count += 1
            if sea_trips_count == number_of_sea_trips:
                sea_is_sold = True
        # else:
        #     sea_is_sold = True
    elif command == "mountain":
        if mountain_trips_count < number_of_mountain_trips:
            mountain_trips_count += 1
            if mountain_trips_count == number_of_mountain_trips:
                mountain_is_sold = True
        # else:
        #     mountain_is_sold = True

    if mountain_is_sold and sea_is_sold:
        break

    command = input()


if mountain_is_sold and sea_is_sold:
    profit = number_of_sea_trips * 680 + number_of_mountain_trips * 499
    print(f"Good job! Everything is sold.")
    print(f"Profit: {profit} leva.")
else:
    if mountain_is_sold:
        profit = sea_trips_count * 680 + number_of_mountain_trips * 499
    elif sea_is_sold:
        profit = number_of_sea_trips * 680 + mountain_trips_count * 499
    else:
        profit = sea_trips_count * 680 + mountain_trips_count * 499
    print(f"Profit: {profit} leva.")