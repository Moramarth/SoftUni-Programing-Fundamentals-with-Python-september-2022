first_list = input().split(", ")
second_list = input().split(", ")

substring_list = list()

for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word:
            substring_list.append(first_word)
            break

print(substring_list)
