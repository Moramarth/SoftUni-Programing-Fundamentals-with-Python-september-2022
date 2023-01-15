number_sequence = list(map(int, input().split(", ")))

current_group = 10

while number_sequence:
    current_result = list()
    for i in range(len(number_sequence)):
        if number_sequence[i] <= current_group:
            current_result.append(number_sequence[i])
    number_sequence = [number for number in number_sequence if number not in current_result]
    print(f"Group of {current_group}'s: {current_result}")
    current_group += 10
