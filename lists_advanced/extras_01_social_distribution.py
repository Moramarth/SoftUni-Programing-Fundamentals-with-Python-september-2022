population = list(map(int, input().split(", ")))

minimum_wealth = int(input())

if sum(population) / len(population) < minimum_wealth:
    print("No equal distribution possible")
    exit()

for index in range(len(population)):
    richest = max(population)
    richest_index = population.index(richest)
    difference = 0
    if population[index] >= minimum_wealth:
        continue

    if population[index] < minimum_wealth:
        difference = minimum_wealth - population[index]

    if richest - difference < minimum_wealth:
        break
    else:
        population[richest_index] -= difference
        population[index] += difference

print(population)
