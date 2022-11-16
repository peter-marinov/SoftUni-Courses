def flights(*args):
    flights_dict = {}
    for index in range(0, len(args), 2):
        if args[index] == 'Finish':
            break

        if args[index] not in flights_dict.keys():
            flights_dict[args[index]] = 0
        flights_dict[args[index]] += int(args[index + 1])

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))