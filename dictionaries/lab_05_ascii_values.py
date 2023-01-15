characters = input().split(", ")

my_dict = {key: ord(key) for key in characters}
print(my_dict)
