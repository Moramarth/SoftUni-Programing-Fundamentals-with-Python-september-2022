text_to_upgrade = input()

characters_only = [char.lower() for char in text_to_upgrade if not char.isdigit()]
unique_chars_used = len(set(characters_only))

rage_burst = ""

current_string = ""

for index in range(len(text_to_upgrade)):
    if not text_to_upgrade[index].isdigit():
        current_string += text_to_upgrade[index]
    else:
        if index != len(text_to_upgrade) - 1:
            if text_to_upgrade[index + 1].isdigit():
                rage_burst += current_string.upper() * int(text_to_upgrade[index] + text_to_upgrade[index + 1])
                current_string = ""
                continue
        rage_burst += current_string.upper() * int(text_to_upgrade[index])
        current_string = ""

print(f"Unique symbols used: {unique_chars_used}")
print(rage_burst)
