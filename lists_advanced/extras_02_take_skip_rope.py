initial_string = input()

numbers_list = [int(number) for number in initial_string if number.isnumeric()]
initial_string = [string for string in initial_string if not string.isnumeric()]
hidden_message = list()

take_list = list()
skip_list = list()


for i in range(len(numbers_list)):
    if i % 2 == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])


for i in range(len(take_list)):
    chars_to_take = take_list[i]
    skipped_chars = skip_list[i]

    hidden_message.extend(initial_string[:chars_to_take])
    initial_string = initial_string[chars_to_take + skipped_chars:]

print("".join(hidden_message))
