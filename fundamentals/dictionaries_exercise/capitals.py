countries = input().split(', ')
cities = input().split(', ')

travel_dict = dict(zip(countries, cities))
output_print = [f'{country} -> {city}' for country, city in travel_dict.items()]
print('\n'.join(output_print))
