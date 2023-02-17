data = input().split(" ")

command = input()

while command != "3:1":
    to_do, *info = command.split()

    if to_do == "merge":
        start_index, end_index = int(info[0]), int(info[1])
        if start_index < 0:
            start_index = 0
        if end_index >= len(data):
            end_index = len(data) - 1

        for i in range(start_index + 1, end_index + 1):
            data[start_index] += data[i]

        data = data[:start_index + 1] + data[end_index + 1:]

    elif to_do == "divide":
        index, parts = int(info[0]), int(info[1])
        item = data.pop(index)

        if parts > len(item):
            step = 1
        else:
            step = len(item) // parts
        current_char = 0
        for part in range(parts):
            if part == parts - 1:
                data.insert(index, item[current_char:])
                break
            else:
                data.insert(index, item[current_char:current_char + step])
            index += 1
            current_char += step

    command = input()

data = [element for element in data if element != ""]
print(" ".join(data))
