string = input()

capitals = []
for i in range(len(string)):
    if 64 < ord(string[i]) < 91:
        capitals.append(i)

print(capitals)
