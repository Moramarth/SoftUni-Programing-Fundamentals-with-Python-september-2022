number_of_lines = int(input())

opening_bracket_count = 0
closing_bracket_count = 0
reset = 0

for _ in range(number_of_lines):
    string = input()
    if opening_bracket_count > 1 or closing_bracket_count > 1:
        continue
    if string == "(":
        opening_bracket_count += 1
    elif string == ")":
        closing_bracket_count += 1
        if opening_bracket_count == 0:
            opening_bracket_count += 5
        if opening_bracket_count == 1:
            reset += 1
            opening_bracket_count = 0
            closing_bracket_count = 0

if reset > 0 and opening_bracket_count == 0 and closing_bracket_count == 0:
    print("BALANCED")
else:
    print("UNBALANCED")



