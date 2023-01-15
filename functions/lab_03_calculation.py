def calculator(operator, num1, num2):
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = int(num1 / num2)
    elif operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    return result


string = input()
first_number = int(input())
second_number = int(input())

print(calculator(string, first_number, second_number))
