number = int(input())


for i in range(1, number + 1):
    current_sum = 0
    new_number = i
    while new_number > 0:
        current_sum += new_number % 10
        new_number = new_number // 10

    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")

