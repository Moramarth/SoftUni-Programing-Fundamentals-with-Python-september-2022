number_of_lines = int(input())

current_capacity = 0

for _ in range(number_of_lines):
    liters = int(input())
    if liters + current_capacity > 255:
        print("Insufficient capacity!")
    else:
        current_capacity += liters

print(current_capacity)
