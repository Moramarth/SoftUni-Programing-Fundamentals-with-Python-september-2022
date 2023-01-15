prepared_gifts = input().split(" ")
command = input()


while command != "No Money":
    variables = command.split(" ")
    current_command = variables[0]
    if current_command == "OutOfStock":
        for i, gift in enumerate(prepared_gifts):
            if gift == variables[1]:
                prepared_gifts[i] = "None"
    elif current_command == "Required":
        if len(prepared_gifts) > int(variables[2]) >= 0:
            prepared_gifts[int(variables[2])] = variables[1]
    elif current_command == "JustInCase":
        prepared_gifts[-1] = variables[1]

    command = input()

gift_list = [gifts for gifts in prepared_gifts if gifts != "None"]
if len(gift_list) > 0:
    print(" ".join(gift_list))
