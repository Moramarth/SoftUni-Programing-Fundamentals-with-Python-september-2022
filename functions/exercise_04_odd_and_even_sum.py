def odd_even_sum(number):
    chars = [ch for ch in number]
    integers = list(map(int, chars))
    odds = [num for num in integers if num % 2 != 0]
    evens = [num for num in integers if num % 2 == 0]
    total_odd = sum(odds)
    total_even = sum(evens)
    result = f"Odd sum = {total_odd}, Even sum = {total_even}"
    return result


random_number = input()

print(odd_even_sum(random_number))
