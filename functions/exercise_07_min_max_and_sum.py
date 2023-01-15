numbers = input().split(" ")

integers = list(map(int, numbers))

smallest = min(integers)
biggest = max(integers)
total = sum(integers)

print(f"The minimum number is {smallest}")
print(f"The maximum number is {biggest}")
print(f"The sum number is: {total}")
