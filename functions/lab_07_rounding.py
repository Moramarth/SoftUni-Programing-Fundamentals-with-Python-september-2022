digits = input().split(" ")

floats = list(map(float, digits))
floats = list(map(round, floats))

print(floats)
