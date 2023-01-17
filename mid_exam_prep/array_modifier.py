list_to_modify = input().split(" ")

integer_list = list(map(int, list_to_modify))

while True:
    command = input()
    if command == "end":
        break
    elif command == "decrease":
        integer_list = list(map(lambda x: x-1, integer_list))
    else:
        to_do, index_one, index_two = command.split(" ")
        if to_do == "swap":
            integer_list[int(index_one)], integer_list[int(index_two)] = \
                integer_list[int(index_two)], integer_list[int(index_one)]
        elif to_do == "multiply":
            multiplier = integer_list[int(index_one)]
            integer_list[int(index_one)] = multiplier * integer_list[int(index_two)]

list_to_modify = [str(integer) for integer in integer_list]

print(', '.join(list_to_modify))
