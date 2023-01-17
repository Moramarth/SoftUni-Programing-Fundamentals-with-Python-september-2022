initial_list = input().split("!")

command = input()

while command != "Go Shopping!":
    operations = command.split()
    to_do = operations[0]
    item = operations[1]
    if to_do == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)
    elif to_do == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)
    elif to_do == "Correct":
        new_item = operations[2]
        if item in initial_list:
            index = initial_list.index(item)
            initial_list.pop(index)
            initial_list.insert(index, new_item)
    elif to_do == "Rearrange":
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)
    command = input()
print(", ".join(initial_list))
