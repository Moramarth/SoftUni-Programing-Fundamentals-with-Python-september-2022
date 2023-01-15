numbers = input().split(", ")

integers = list(map(int, numbers))
indices = list()

for i, integer in enumerate(integers):
    if integer % 2 == 0:
        indices.append(i)

print(indices)
