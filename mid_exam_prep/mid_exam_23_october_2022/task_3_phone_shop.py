storage = input().split(", ")

command = input()

while command != "End":
    to_do, phone = command.split(" - ")
    if to_do == "Add":
        if phone not in storage:
            storage.append(phone)
    elif to_do == "Remove":
        if phone in storage:
            storage.remove(phone)
    elif to_do == "Bonus phone":
        old_phone, new_phone = phone.split(":")
        if old_phone in storage:
            index = storage.index(old_phone)
            storage.insert(index + 1, new_phone)
    elif to_do == "Last":
        if phone in storage:
            storage.remove(phone)
            storage.append(phone)

    command = input()

print(", ".join(storage))
