usernames = input().split(", ")

legal = ["_", "-"]

for username in usernames:
    valid = True
    if not 3 <= len(username) <= 16:
        continue
    for char in username:
        if not char.isdigit() and not char.isalpha() and char not in legal:
            valid = False

    if valid:
        print(username)
