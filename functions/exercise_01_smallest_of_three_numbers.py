def smallest_number(a, b, c):
    group = [a, b, c]
    result = min(group)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())


print(smallest_number(first_number, second_number, third_number))
