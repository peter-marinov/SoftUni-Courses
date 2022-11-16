import re

string = input()

# pattern = r'=([A-Z][a-zA-z]{2,})=|\/([A-Z][a-zA-z]{2,})\/'
pattern = r'([=\/])([A-Z][a-zA-z]{2,})\1'

result = re.findall(pattern, string)
destination_list = []
travel_points = 0
for destination in result:
    travel_points += len(destination[1])
    destination_list.append(destination[1])

print(f"Destinations: {', '.join(destination_list)}")
print(f"Travel Points: {travel_points}")
