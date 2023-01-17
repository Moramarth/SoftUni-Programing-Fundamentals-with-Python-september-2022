encrypted_skill = input()

command = input()

while command != "For Azeroth":

    data = command.split()
    to_do = data[0]
    if to_do == "GladiatorStance":
        encrypted_skill = encrypted_skill.upper()
        print(encrypted_skill)
    elif to_do == "DefensiveStance":
        encrypted_skill = encrypted_skill.lower()
        print(encrypted_skill)
    elif to_do == "Dispel":
        index, letter = int(data[1]), data[2]
        if 0 <= index < len(encrypted_skill):
            encrypted_skill = encrypted_skill[:index] + letter + encrypted_skill[index + 1:]
            print("Success!")
        else:
            print("Dispel too weak.")
    elif to_do == "Target":
        if data[1] == "Change":
            first_string, second_string = data[2], data[3]
            if first_string in encrypted_skill:
                encrypted_skill = encrypted_skill.replace(first_string, second_string)
            print(encrypted_skill)
        elif data[1] == "Remove":
            substring = data[2]
            if substring in encrypted_skill:
                encrypted_skill = encrypted_skill.replace(substring, "")
                print(encrypted_skill)
        else:
            print("Command doesn't exist!")
    else:
        print("Command doesn't exist!")

    command = input()