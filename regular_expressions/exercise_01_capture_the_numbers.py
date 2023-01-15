import re

extracted_numbers = list()
pattern = r"\d+"

line = input()
while line:
    matches = re.findall(pattern, line)
    extracted_numbers.extend(matches)
    line = input()

print(" ".join(extracted_numbers))
