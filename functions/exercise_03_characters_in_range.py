def chars_in_range(a, b):
    start = ord(a)
    end = ord(b)
    chars = [chr(num) for num in range(start + 1, end)]
    string = " ".join(chars)
    return string


first = input()
second = input()

print(chars_in_range(first, second))
