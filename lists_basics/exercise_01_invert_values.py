strings = input().split(" ")

numbers = list()

for char in strings:
    if int(char) >= 0:
        numbers.append(-int(char))
    else:
        numbers.append(abs(int(char)))

print(numbers)
