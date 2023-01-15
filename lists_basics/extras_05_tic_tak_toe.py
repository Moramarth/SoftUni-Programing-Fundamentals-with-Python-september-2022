def row_win_condition(row):
    if len(set(row)) == 1:
        if row[0] == "1":
            print("First player won")
            quit()
        elif row[0] == "2":
            print("Second player won")
            quit()


def diagonal_win(row_1, row_2, row_3):
    if row_1[0] == row_2[1] and row_1[0] == row_3[2]:
        if row_1[0] == "1":
            print("First player won")
            quit()
        elif row_1[0] == "2":
            print("Second player won")
            quit()
    elif row_1[2] == row_2[1] and row_1[2] == row_3[0]:
        if row_1[2] == "1":
            print("First player won")
            quit()
        elif row_1[2] == "2":
            print("Second player won")
            quit()


first_row = input().split(" ")
second_row = input().split(" ")
third_row = input().split(" ")


row_win_condition(first_row)
row_win_condition(second_row)
row_win_condition(third_row)

diagonal_win(first_row, second_row, third_row)

# columns conditions
for spot_1, spot_2, spot_3 in zip(first_row, second_row, third_row):
    if spot_1 == spot_2 and spot_1 == spot_3:
        if spot_1 == "1":
            print("First player won")
            quit()
        elif spot_1 == "2":
            print("Second player won")
            quit()
# Draw
print("Draw!")
