first = int(input())
second = int(input())
third = int(input())

numbers = [first, second, third]
negatives = [num for num in numbers if num < 0]
if 0 in numbers:
    print("zero")
elif len(negatives) % 2 == 0:
    print("positive")
elif len(negatives) % 2 != 0:
    print("negative")
else:
    print("positive")

