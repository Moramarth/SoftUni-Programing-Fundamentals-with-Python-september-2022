import re

phone_numbers = input()

requirements = r"(\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4})\b"

matches = re.findall(requirements, phone_numbers)

print(", ".join(matches))
