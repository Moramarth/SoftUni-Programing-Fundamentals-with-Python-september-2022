def house_status_func(index, houses):
    if neighbourhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        neighbourhood[index] -= 2
        if neighbourhood[index] == 0:
            print(f"Place {index} has Valentine's day.")
    return houses


neighbourhood = list(map(int, input().split("@")))

current_index = 0
command = input()

while command != "Love!":
    distance = int(command.split()[1])
    if distance + current_index >= len(neighbourhood):
        current_index = 0
        neighbourhood = house_status_func(current_index, neighbourhood)
    else:
        current_index += distance
        neighbourhood = house_status_func(current_index, neighbourhood)
    command = input()

print(f"Cupid's last position was {current_index}.")
final_state_of_houses = [house for house in neighbourhood if house != 0]
if not final_state_of_houses:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(final_state_of_houses)} places.")
