number_of_strings = int(input())
key_word = input()

strings = list()
filtered_strings = list()

for _ in range(number_of_strings):
    current_string = input()
    strings.append(current_string)
    if key_word in current_string:
        filtered_strings.append(current_string)


print(strings)
print(filtered_strings)
