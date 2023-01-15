string = input().replace(" ", "")

my_dict = dict()

for char in string:
    if char not in my_dict:
        my_dict[char] = 1
    else:
        my_dict[char] += 1

for key in my_dict:
    print(f"{key} -> {my_dict[key]}")
