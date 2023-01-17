random_string = input()

command = input()

while command != "Travel":
    data = command.split(":")
    to_do = data[0]
    if to_do == "Add Stop":
        index, string = int(data[1]), data[2]
        if 0 <= index < len(random_string):
            random_string = random_string[:index] + string + random_string[index:]
    elif to_do == "Remove Stop":
        start_index, end_index = int(data[1]), int(data[2])
        if 0 <= start_index <= end_index < len(random_string):
            random_string = random_string[:start_index] + random_string[end_index + 1:]
    elif to_do == "Switch":
        old_string, new_string = data[1], data[2]
        random_string = random_string.replace(old_string, new_string)

    print(random_string)

    command = input()

print(f"Ready for world tour! Planned stops: {random_string}")
