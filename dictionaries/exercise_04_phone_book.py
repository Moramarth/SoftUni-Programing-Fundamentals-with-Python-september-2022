to_search = 0

phonebook = dict()
while True:
    data = input().split("-")
    if len(data) == 1:
        to_search = int(data[0])
        break
    name = data[0]
    phone_number = data[1]
    phonebook[name] = phone_number

for i in range(to_search):
    name = input()
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
