random_string = input()

command = input()

while command != "Done":
    data = command.split()
    to_do = data[0]
    if to_do == "Change":
        char, replacement = data[1], data[2]
        random_string = random_string.replace(char, replacement)
        print(random_string)
    elif to_do == "Includes":
        substring = data[1]
        if substring in random_string:
            print("True")
        else:
            print("False")
    elif to_do == "End":
        substring = data[1]
        if substring == random_string[len(random_string)-len(substring):]:
            print("True")
        else:
            print("False")
    elif to_do == "Uppercase":
        random_string = random_string.upper()
        print(random_string)
    elif to_do == "FindIndex":
        char = data[1]
        index = random_string.find(char)
        print(index)
    elif to_do == "Cut":
        start_index, length = int(data[1]), int(data[2])
        random_string = random_string[start_index:start_index + length]
        print(random_string)

    command = input()
