string_of_integers = input().split(" ")
numbers_to_remove = int(input())

list_of_numbers = list(map(int, string_of_integers))

for _ in range(numbers_to_remove):
    current_element = min(list_of_numbers)
    list_of_numbers.remove(current_element)
    string_of_integers.remove(str(current_element))

print(", ".join(string_of_integers))
