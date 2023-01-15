command = input()

bakery = dict()

while command != "statistics":
    data = command.split(": ")
    key = data[0]
    value = data[1]
    if key in bakery:
        bakery[key] += int(value)
    else:
        bakery[key] = int(value)
    command = input()

print("Products in stock:")

for (key, value) in bakery.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")
