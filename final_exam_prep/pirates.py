world_map = dict()

command = input()

while command != "Sail":

    city, population, gold = command.split("||")
    if city in world_map:
        world_map[city][0] += int(population)
        world_map[city][1] += int(gold)
    else:
        world_map[city] = [int(population), int(gold)]
    command = input()

next_command = input()

while next_command != "End":
    data = next_command.split("=>")
    to_do = data[0]
    city = data[1]
    if to_do == "Plunder":
        people, gold = int(data[2]), int(data[3])
        world_map[city][0] -= people
        world_map[city][1] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if world_map[city][0] == 0 or world_map[city][1] == 0:
            print(f"{city} has been wiped off the map!")
            del world_map[city]
    elif to_do == "Prosper":
        gold = int(data[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            world_map[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {world_map[city][1]} gold.")

    next_command = input()

if not world_map:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(world_map)} wealthy settlements to go to:")
    for city in world_map:
        print(f"{city} -> Population: {world_map[city][0]} citizens, Gold: {world_map[city][1]} kg")
