number_of_rows = int(input())

ocean = list()
ships_destroyed = 0

for row_number in range(number_of_rows):
    ocean.append([int(number) for number in input().split()])

coordinates = input().split()

for pair in coordinates:
    data = pair.split("-")
    row, column = int(data[0]), int(data[1])

    if ocean[row][column] == 0:
        continue

    ocean[row][column] -= 1
    if ocean[row][column] == 0:
        ships_destroyed += 1

print(ships_destroyed)
