def validator(password):
    digit_count = 0
    is_valid = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    for ch in password:
        if ch.isdigit():
            digit_count += 1
    if digit_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid


pass_code = input()

if validator(pass_code):
    print("Password is valid")
