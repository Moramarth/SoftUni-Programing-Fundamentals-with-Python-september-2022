names = input().split(", ")
new_list = sorted(names, key=lambda x: (-len(x), x))
print(new_list)
