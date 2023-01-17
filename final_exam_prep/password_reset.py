password = input()
command = input()

while command != "Done":
    data = command.split()
    to_do = data[0]
    if to_do == "TakeOdd":
        raw_password = ""
        for index in range(len(password)):
            if index % 2 != 0:
                raw_password += password[index]
        password = raw_password
        print(password)
    elif to_do == "Cut":
        index, length = int(data[1]), int(data[2])
        substring = password[index:index + length]
        password = password.replace(substring, "", 1)
        print(password)
    elif to_do == "Substitute":
        substring, replacement = data[1], data[2]
        if substring in password:
            password = password.replace(substring, replacement)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {password}")
