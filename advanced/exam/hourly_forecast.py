def forecast(*args):
    print(args)
    cities_sunny = {}
    cities_cloudy = {}
    cities_rainy = {}
    for data in args:
        if data[1] == 'Sunny':
            cities_sunny[data[0]] = data[1]
        elif data[1] == 'Cloudy':
            cities_cloudy[data[0]] = data[1]
        elif data[1] == 'Rainy':
            cities_rainy[data[0]] = data[1]

    cities_sunny = dict(sorted(cities_sunny.items(), key=lambda x: x[0]))
    cities_cloudy = dict(sorted(cities_cloudy.items(), key=lambda x: x[0]))
    cities_rainy = dict(sorted(cities_rainy.items(), key=lambda x: x[0]))

    output_sting = ''
    for key, value in cities_sunny.items():
        output_sting += f'{key} - {value}\n'

    for key, value in cities_cloudy.items():
        output_sting += f'{key} - {value}\n'

    for key, value in cities_rainy.items():
        output_sting += f'{key} - {value}\n'

    return output_sting.strip()


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")),)