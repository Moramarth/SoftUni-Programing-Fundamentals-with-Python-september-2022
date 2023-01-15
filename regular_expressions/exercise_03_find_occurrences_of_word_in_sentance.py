import re

random_sentence = input()
word = input()

pattern = fr"\b{word}\b"

matches = re.findall(pattern, random_sentence, re.IGNORECASE)

print(len(matches))
