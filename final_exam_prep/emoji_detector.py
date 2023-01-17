import re

random_string = input()

digit_pattern = r"\d"
emoji_pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"

cool_threshold = 1

digits = re.findall(digit_pattern, random_string)

for digit in digits:
    cool_threshold *= int(digit)

print(f"Cool threshold: {cool_threshold}")

emojis = re.findall(emoji_pattern, random_string)

print(f"{len(emojis)} emojis found in the text. The cool ones are:")

for emoji in emojis:
    cool_factor = 0
    for char in emoji[1]:
        cool_factor += ord(char)
    if cool_factor >= cool_threshold:
        print("".join(emoji))
