secret_message = input()

words = secret_message.split(" ")

message = list()

for word in words:
    digits = ""
    chars = list()
    for char in word:
        if char.isdigit():
            digits += char
        elif char.isalpha():
            chars.append(char)
    chars[0], chars[-1] = chars[-1], chars[0]
    message.append(chr(int(digits)) + "".join(chars))

print(" ".join(message))
