starting_year = int(input())

current_year = starting_year

while True:
    current_year += 1
    year_digits = str(current_year)
    set_digit = set(year_digits)
    if len(year_digits) == len(set_digit):
        print(current_year)
        break
