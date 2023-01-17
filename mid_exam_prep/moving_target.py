def shoot_command_func(index, power, targets):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets


def add_command_func(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")
    return targets


def strike_command_func(index, radius, targets):
    if 0 > index - radius or len(targets) <= index + radius:
        print("Strike missed!")
    else:
        # for target in range(len(targets)-1, -1, -1):
        #     if index - radius <= target <= index + radius:
        #         targets.pop(target)
        del targets[index - radius:index + radius + 1]
    return targets


def shooting_targets_func(targets):
    while True:
        command = input()
        if command == "End":
            break
        to_do, index, value = command.split(" ")
        if to_do == "Shoot":
            shoot_command_func(int(index), int(value), targets)
        elif to_do == "Add":
            add_command_func(int(index), int(value), targets)
        elif to_do == "Strike":
            strike_command_func(int(index), int(value), targets)
    targets = list(map(str, targets))
    return targets


data = list(map(int, input().split()))
final_data = shooting_targets_func(data)
print("|".join(final_data))
