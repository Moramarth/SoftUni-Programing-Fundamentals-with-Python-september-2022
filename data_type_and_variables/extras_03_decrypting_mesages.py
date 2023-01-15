key = int(input())
number_of_characters = int(input())

result = []

for _ in range(number_of_characters):
    char = input()
    new_char = chr(ord(char) + key)
    result.append(new_char)

message = "".join(result)

print(message)
