import re

random_string = input()
pattern = r"(#|@)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

matches = re.findall(pattern, random_string)

mirror_words = list()

for match in matches:
    if match[1] == match[2][::-1]:
        mirror_words.append(f"{match[1]} <=> {match[2]}")

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))
