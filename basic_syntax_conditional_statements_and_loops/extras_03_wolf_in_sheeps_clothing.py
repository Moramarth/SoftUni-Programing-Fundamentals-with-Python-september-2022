string = input()

animals = list(string.split(", "))
count = 1
for animal in animals:
    if animal == "wolf" and count == len(animals):
        print("Please go away and stop eating my sheep")
    elif animal == "wolf":
        sheep = abs(len(animals) - count)
        print(f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!")
    count += 1
