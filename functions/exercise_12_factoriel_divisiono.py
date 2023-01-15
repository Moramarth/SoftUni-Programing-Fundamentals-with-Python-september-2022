from math import factorial


def factorial_division(num1, num2):
    return factorial(num1) / factorial(num2)


first_number = int(input())
second_number = int(input())

final_calculation = factorial_division(first_number, second_number)
print(f"{final_calculation:.2f}")
