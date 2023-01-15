number_of_strings_to_check = int(input())

string_is_pure = True
for check in range(number_of_strings_to_check):
    string_is_pure = True
    string = input()
    for char in string:
        if char == "," or char == "_" or char == ".":
            string_is_pure = False
    if string_is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
