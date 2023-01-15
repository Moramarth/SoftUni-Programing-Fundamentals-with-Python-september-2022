string = input()

characters = [char for char in string]

for index in range(len(characters) - 1, 0, -1):
    if characters[index] == characters[index - 1]:
        characters.pop(index)

print("".join(characters))
