distance_to_pokemons = list(map(int, input().split()))

total_sum_of_removed_pokemon = 0

while distance_to_pokemons:
    index_for_removal = int(input())

    if 0 <= index_for_removal < len(distance_to_pokemons):
        value = distance_to_pokemons.pop(index_for_removal)
        total_sum_of_removed_pokemon += value
        distance_to_pokemons = [distance + value if distance <= value else distance-value
                                for distance in distance_to_pokemons]

    elif index_for_removal < 0:
        value = distance_to_pokemons.pop(0)
        total_sum_of_removed_pokemon += value
        distance_to_pokemons.insert(0, distance_to_pokemons[-1])
        distance_to_pokemons = [distance + value if distance <= value else distance - value
                                for distance in distance_to_pokemons]

    else:
        value = distance_to_pokemons.pop()
        total_sum_of_removed_pokemon += value
        distance_to_pokemons.append(distance_to_pokemons[0])
        distance_to_pokemons = [distance + value if distance <= value else distance - value
                                for distance in distance_to_pokemons]

print(total_sum_of_removed_pokemon)
