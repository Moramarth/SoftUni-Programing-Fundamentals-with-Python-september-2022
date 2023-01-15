def perfect_checker(num):
    binary = bin(num)[2:]
    binary_list = [num for num in binary]
    last_one = 0
    for i, char in enumerate(binary_list):
        if char == "1":
            last_one = i
    ones = binary_list[:last_one + 1]
    zeros = binary_list[last_one + 1:]
    if set(ones) == {"1"} and set(zeros) == {"0"}:
        if len(ones) == (len(zeros) + 1):
            print("We have a perfect number!")
        else:
            print("It's not so perfect.")
    else:
        print("It's not so perfect.")


number = int(input())

perfect_checker(number)
