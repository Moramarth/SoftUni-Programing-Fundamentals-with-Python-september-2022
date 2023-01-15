string = input().lower()

count = 0

for i, _ in enumerate(string):
    if string[i:i+len("water")] == "water":
        count += 1
for i, _ in enumerate(string):
    if string[i:i+len("sand")] == "sand":
        count += 1
for i, _ in enumerate(string):
    if string[i:i+len("fish")] == "fish":
        count += 1
for i, _ in enumerate(string):
    if string[i:i+len("sun")] == "sun":
        count += 1

print(count)
