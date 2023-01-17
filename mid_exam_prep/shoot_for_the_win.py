def change_targets_score_func(score, sequence):
    integer_list = list(map(int, sequence))
    for i, integer in enumerate(integer_list):
        if integer == -1:
            continue
        elif integer > score:
            integer_list[i] -= score
        elif integer <= score:
            integer_list[i] += score
    sequence = list(map(str, integer_list))
    return sequence


def hit_target_func(integer, sequence):
    score = int(sequence[integer])
    sequence[integer] = "-1"
    sequence = change_targets_score_func(score, sequence)
    return sequence


def validator_func(integer, sequence):
    is_valid = True
    if integer < 0 or integer >= len(sequence):
        is_valid = False
    return is_valid


def shooting_targets_func(targets):
    count = 0
    while True:
        command = input()
        if command == "End":
            print(f"Shot targets: {count} -> {' '.join(targets)}")
            break
        index = int(command)
        if not validator_func(index, targets):
            continue
        if targets[index] != "-1":
            count += 1
            targets = hit_target_func(index, targets)
        else:
            continue


data = input().split()
shooting_targets_func(data)
