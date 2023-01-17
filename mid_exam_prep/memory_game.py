def validator_func(first_index, second_index, sequence):
    is_valid = True
    if 0 > int(first_index) or len(sequence) <= int(first_index):
        is_valid = False
    if 0 > int(second_index) or len(sequence) <= int(second_index):
        is_valid = False
    if first_index == second_index:
        is_valid = False
    if not is_valid:
        print("Invalid input! Adding additional elements to the board")
        mid_index = len(sequence) // 2
        sequence.insert(mid_index, f"-{number_of_moves}a")
        sequence.insert(mid_index, f"-{number_of_moves}a")
    return is_valid, sequence


def check_if_matching_func(first_index, second_index, sequence):
    index_one = int(first_index)
    index_two = int(second_index)
    if sequence[index_one] == sequence[index_two]:
        element = sequence[index_one]
        print(f"Congrats! You have found matching elements - {element}!")
        sequence.remove(element)
        sequence.remove(element)
    else:
        print("Try again!")
    return sequence


elements_sequence = input().split(" ")

number_of_moves = 0
game_won = False
while True:
    command = input()
    if command == "end":
        break
    number_of_moves += 1
    first_integer, second_integer = command.split(" ")

    validation, elements_sequence = validator_func(first_integer, second_integer, elements_sequence)
    if not validation:
        continue

    check_if_matching_func(first_integer, second_integer, elements_sequence)
    if not elements_sequence:
        print(f"You have won in {number_of_moves} turns!")
        game_won = True
        break

if not game_won:
    print("Sorry you lose :(")
    print(" ".join(elements_sequence))
