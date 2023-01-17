import re

random_string = input()
pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"

destinations = list()
travel_points = 0

matches = re.findall(pattern, random_string)
for match in matches:
    destinations.append(match[1])
    travel_points += len(match[1])

print(f'Destinations: {", ".join(destinations)}')
print(f"Travel Points: {travel_points}")
