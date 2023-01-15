import re

random_sentence = input()

pattern = r"\s(([A-Za-z0-9])+([\.\-\_])?([A-Za-z0-9])+?@([A-Za-z0-9\-])+\.([A-Za-z0-9])+(\.([A-Za-z0-9])+)?)"

matches = re.findall(pattern,random_sentence)

for match in matches:
    print(match[0])
