group_size = int(input())
days = int(input())

current_coins = 0

for day in range(1, days + 1):
    current_coins += 50
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    current_coins -= 2 * group_size
    if day % 3 == 0:
        current_coins -= 3 * group_size
    if day % 5 == 0:
        current_coins += 20 * group_size
        if day % 3 == 0:
            current_coins -= 2 * group_size

coins = current_coins // group_size

print(f"{group_size} companions received {coins} coins each.")
