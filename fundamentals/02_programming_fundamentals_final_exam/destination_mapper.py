import re

destinations = input()

search_pattern = r'([=\/])([A-Z][a-zA-Z]{2,})\1'
filtered_destinations = []
travel_points = 0
for match in re.finditer(search_pattern, destinations):
    filtered_destinations.append(match.group(2))
    travel_points += len(match.group(2))

result = ', '.join(filtered_destinations)
print(f'Destinations: {result}')
print(f'Travel Points: {travel_points}')