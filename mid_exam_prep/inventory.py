collected_items = input().split(", ")

command = input()

while command != "Craft!":
    to_do, item = command.split(" - ")
    if to_do == "Collect":
        if item not in collected_items:
            collected_items.append(item)
    elif to_do == "Drop":
        if item in collected_items:
            collected_items.remove(item)
    elif to_do == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in collected_items:
            index = collected_items.index(old_item)
            collected_items.insert(index + 1, new_item)
    elif to_do == "Renew":
        if item in collected_items:
            collected_items.remove(item)
            collected_items.append(item)
    command = input()
print((", ".join(collected_items)))
