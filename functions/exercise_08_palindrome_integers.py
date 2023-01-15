def palindrome(list_of_numbers):
    for num in list_of_numbers:
        current_check = [ch for ch in num]
        backward_check = list(reversed(current_check))
        if current_check == backward_check:
            print(True)
        else:
            print(False)


numbers = input().split(", ")

palindrome(numbers)
