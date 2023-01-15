from itertools import cycle, islice


def min_max_index(source, number):
    last_match = 0
    for i, element in enumerate(source):
        if element == number:
            last_match = i
    return last_match


def first_choices(source, number):
    current_list = list()
    for i, element in enumerate(source):
        if i < number:
            current_list.append(element)
    return current_list


def last_choices(source, number):
    current_list = list()
    source.reverse()
    for i, element in enumerate(source):
        if i < number:
            current_list.append(element)
    current_list.reverse()
    return current_list


to_manipulate = input().split(" ")

integer_list = list(map(int, to_manipulate))

command = input()

while command != "end":
    to_do = command.split(" ")
    if to_do[0] == "exchange":  # {index}
        if 0 <= int(to_do[1]) < len(integer_list):
            integer_list = list(islice(cycle(integer_list), int(to_do[1]) + 1, int(to_do[1]) + 1 + len(integer_list)))
        else:
            print("Invalid index")
    elif to_do[0] == "max":  # even/odd
        if to_do[1] == "odd":
            odd_list = [odd for odd in integer_list if odd % 2 != 0]
            if not odd_list:
                print("No matches")
            else:
                needed_max = max(odd_list)
                print(min_max_index(integer_list, needed_max))
        else:
            even_list = [even for even in integer_list if even % 2 == 0]
            if not even_list:
                print("No matches")
            else:
                needed_max = max(even_list)
                print(min_max_index(integer_list, needed_max))
    elif to_do[0] == "min":  # even/odd
        if to_do[1] == "odd":
            odd_list = [odd for odd in integer_list if odd % 2 != 0]
            if not odd_list:
                print("No matches")
            else:
                needed_min = min(odd_list)
                print(min_max_index(integer_list, needed_min))
        else:
            even_list = [even for even in integer_list if even % 2 == 0]
            if not even_list:
                print("No matches")
            else:
                needed_min = min(even_list)
                print(min_max_index(integer_list, needed_min))
    elif to_do[0] == "first":  # {count} even/odd
        if int(to_do[1]) > len(integer_list):
            print("Invalid count")
        else:
            if to_do[2] == "odd":
                odd_list = [odd for odd in integer_list if odd % 2 != 0]
                if not odd_list:
                    print(odd_list)
                else:
                    print(first_choices(odd_list, int(to_do[1])))
            else:
                even_list = [even for even in integer_list if even % 2 == 0]
                if not even_list:
                    print(even_list)
                else:
                    print(first_choices(even_list, int(to_do[1])))
    elif to_do[0] == "last":  # {count} even/odd
        if int(to_do[1]) > len(integer_list):
            print("Invalid count")
        else:
            if to_do[2] == "odd":
                odd_list = [odd for odd in integer_list if odd % 2 != 0]
                if not odd_list:
                    print(odd_list)
                else:
                    print(last_choices(odd_list, int(to_do[1])))
            else:
                even_list = [even for even in integer_list if even % 2 == 0]
                if not even_list:
                    print(even_list)
                else:
                    print(last_choices(even_list, int(to_do[1])))

    command = input()

print(integer_list)
