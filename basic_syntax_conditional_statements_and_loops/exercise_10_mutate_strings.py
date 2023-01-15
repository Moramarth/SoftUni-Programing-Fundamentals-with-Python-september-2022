first_string = input()
second_string = input()

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        replacement = second_string[i]
        new_word = first_string[0:i] + replacement + first_string[i + 1:]
        first_string = new_word
        print(first_string)
