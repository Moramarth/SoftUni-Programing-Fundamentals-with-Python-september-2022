def sum_numbers(a, b):
    return a+b


def subtract(previous, c):
    return previous - c


def add_and_subtract(a, b, c):
    result = subtract(sum_numbers(a, b), c)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
