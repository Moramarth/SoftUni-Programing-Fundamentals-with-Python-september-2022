resource = input()

total_resources = dict()

while resource != "stop":
    quantity = int(input())

    if resource not in total_resources:
        total_resources[resource] = quantity
    else:
        total_resources[resource] += quantity
    resource = input()

for key in total_resources:
    print(f"{key} -> {total_resources[key]}")
