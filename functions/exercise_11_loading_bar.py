def loading(number):
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        index = number // 10
        print(f"{number}% [", end="")
        for i in range(1, 11):
            if i <= index:
                print("%", end="")
            else:
                print(".", end="")
        print("]")
        print("Still loading...")


percent = int(input())

loading(percent)
