def result_func(dictionary):
    result = "Plants for the exhibition:\n"
    for plant in dictionary:
        if dictionary[plant][1]:
            average_rating = sum(dictionary[plant][1]) / len(dictionary[plant][1])
        else:
            average_rating = 0
        result += f"- {plant}; Rarity: {dictionary[plant][0]}; Rating: {average_rating:.2f}\n"
    return result


def reset_func(dictionary, plant):
    if plant not in dictionary.keys():
        print("error")
    else:
        dictionary[plant][1] = []


def update_func(dictionary, plant, rarity):
    if plant not in dictionary.keys():
        print("error")
    else:
        dictionary[plant][0] = rarity


def rate_func(dictionary, plant, rating):
    if plant not in dictionary.keys():
        print("error")
    else:
        dictionary[plant][1].append(int(rating))


def plant_sorting_func(number):
    plants_dict = dict()
    for _ in range(number):
        data = input().split("<->")
        plant, rarity = data[0], data[1]
        plants_dict[plant] = [rarity,  []]
    command = input()

    while command != "Exhibition":
        to_do, additional_information = command.split(": ")
        if to_do == "Rate":
            plant, rating = additional_information.split(" - ")
            rate_func(plants_dict, plant, rating)
        elif to_do == "Update":
            plant, new_rarity = additional_information.split(" - ")
            update_func(plants_dict, plant, new_rarity)
        elif to_do == "Reset":
            plant = additional_information
            reset_func(plants_dict, plant)

        command = input()

    print(result_func(plants_dict))


number_of_plants = int(input())
plant_sorting_func(number_of_plants)
