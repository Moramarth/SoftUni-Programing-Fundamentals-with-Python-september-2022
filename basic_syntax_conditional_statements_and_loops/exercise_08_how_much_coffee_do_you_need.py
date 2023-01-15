needed_coffee = 0

while True:
    event = input()
    if event == "END":
        break
    elif event not in ["dog", "cat", "coding", "movie", "DOG", "CAT", "CODING", "MOVIE"]:
        continue
    if event in ["dog", "cat", "coding", "movie"]:
        needed_coffee += 1
    else:
        needed_coffee += 2

if needed_coffee > 5:
    print("You need extra sleep")
else:
    print(needed_coffee)
