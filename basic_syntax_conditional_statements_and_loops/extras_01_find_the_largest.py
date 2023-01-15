number = input()

digits = []

for char in number:
    digits.append(char)

max_number = sorted(digits, reverse=True)

print("".join(max_number))
