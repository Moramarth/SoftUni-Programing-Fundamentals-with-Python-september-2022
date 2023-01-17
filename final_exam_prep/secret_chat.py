concealed_message = input()

instructions = input()

while instructions != "Reveal":

    data = instructions.split(":|:")

    if data[0] == "InsertSpace":
        index = int(data[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif data[0] == "Reverse":
        substring = data[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message = concealed_message + substring[::-1]
            print(concealed_message)
        else:
            print("error")
    elif data[0] == "ChangeAll":
        substring, replacement = data[1], data[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    instructions = input()

print(f"You have a new text message: {concealed_message}")
