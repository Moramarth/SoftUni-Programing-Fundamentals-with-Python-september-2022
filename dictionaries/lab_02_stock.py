data = input().split()
needed_info = input().split()

stock = dict()

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    stock[key] = int(value)

for item in needed_info:
    if item in stock:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
