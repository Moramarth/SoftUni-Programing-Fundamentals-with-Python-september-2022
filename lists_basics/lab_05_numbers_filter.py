integers_count = int(input())

even = list()
odd = list()
positive = list()
negative = list()

for _ in range(integers_count):
    current_integer = int(input())
    if current_integer % 2 == 0:
        even.append(current_integer)
    else:
        odd.append(current_integer)
    if current_integer >= 0:
        positive.append(current_integer)
    else:
        negative.append(current_integer)


command = input()

print(eval(command))
