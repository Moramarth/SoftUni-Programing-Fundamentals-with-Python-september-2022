activation_key = input()

command = input()

while command != "Generate":

    data = command.split(">>>")
    to_do = data[0]

    if to_do == "Contains":
        substring = data[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif to_do == "Flip":
        case, start_index, end_index = data[1],int(data[2]), int(data[3])
        if case == "Upper":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper()\
                             + activation_key[end_index:]
        elif case == "Lower":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() \
                             + activation_key[end_index:]
        print(activation_key)
    elif to_do == "Slice":
        start_index, end_index = int(data[1]), int(data[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
