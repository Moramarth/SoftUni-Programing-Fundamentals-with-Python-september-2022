countries = input().split(", ")
cities = input().split(", ")
merged = list(zip(countries, cities))

my_dict = {key: value for (key, value) in merged}

for key in my_dict:
    print(f"{key} -> {my_dict[key]}")
