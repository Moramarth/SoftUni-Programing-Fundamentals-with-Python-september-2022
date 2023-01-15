number_of_wagons = int(input())

train = [0 for num in range(number_of_wagons)]

command = input()

while command != "End":
    current_to_do = command.split(" ")

    if current_to_do[0] == "add":
        train[-1] += int(current_to_do[1])
    elif current_to_do[0] == "insert":
        index = int(current_to_do[1])
        train[index] += int(current_to_do[2])
    elif current_to_do[0] == "leave":
        index = int(current_to_do[1])
        train[index] -= int(current_to_do[2])

    command = input()
else:
    print(train)
