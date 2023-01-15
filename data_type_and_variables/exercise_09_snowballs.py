snowball_count = int(input())

best_snowball = 0
snowball_data = ""

for _ in range(snowball_count):
    weight = int(input())
    time = int(input())
    quality = int(input())
    result = int((weight / time) ** quality)
    if result > best_snowball:
        best_snowball = result
        snowball_data = f"{weight} : {time} = {result} ({quality})"

print(snowball_data)
