import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

names = input()

result = re.findall(pattern, names)

print(" ".join(result))
