import re

number_of_strings = int(input())

pattern = r"(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1"

for _ in range(number_of_strings):
    password = input()
    validator = re.findall(pattern, password)
    if not validator:
        print("Try another password!")
    else:
        encrypted_password = validator[0][1] + validator[0][2] + validator[0][3] + validator[0][4]
        print(f"Password: {encrypted_password}")
