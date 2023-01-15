first_string, second_string = input().split()

final_result = 0

digits_first = [ord(char) for char in first_string]
digits_second = [ord(char) for char in second_string]
if len(digits_first) > len(digits_second):
    while len(digits_first) != (len(digits_second)):
        digits_second.append(1)
elif len(digits_second) > len(digits_first):
    while len(digits_first) != (len(digits_second)):
        digits_first.append(1)
combined_digits = list(zip(digits_first, digits_second))
for (first, second) in combined_digits:
    final_result += first*second

print(final_result)
