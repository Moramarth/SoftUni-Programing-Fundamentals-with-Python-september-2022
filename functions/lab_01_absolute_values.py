def absolute_values(source):
    new_list = [abs(num) for num in source]
    return new_list


numbers = input().split(" ")
floats = list(map(float, numbers))
print(absolute_values(floats))
