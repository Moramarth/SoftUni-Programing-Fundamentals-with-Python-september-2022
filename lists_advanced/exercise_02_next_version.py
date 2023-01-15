version = input().split(".")

numbers = list(map(int, version))

for index in range(len(numbers) - 1, -1, -1):
    if numbers[index] + 1 <= 9:
        numbers[index] += 1
        break
    else:
        numbers[index] = 0

numbers = list(map(str, numbers))
print(".".join(numbers))
