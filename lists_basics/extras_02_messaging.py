def sum_search(index):
    current_sum = 0
    for ch in number_sequence[index]:
        current_sum += int(ch)
    return current_sum


def removing_character(index):
    list_of_chars = [ch for ch in random_string]
    list_of_chars.pop(index)
    new_string = "".join(list_of_chars)
    return new_string


number_sequence = input().split(" ")

random_string = input()
message = ""

for i in range(len(number_sequence)):
    tracker = sum_search(i)
    if len(random_string) <= tracker:
        while len(random_string) <= tracker:
            tracker -= len(random_string)
        message += random_string[tracker]
    else:
        message += random_string[tracker]

    random_string = removing_character(tracker)

print(message)
