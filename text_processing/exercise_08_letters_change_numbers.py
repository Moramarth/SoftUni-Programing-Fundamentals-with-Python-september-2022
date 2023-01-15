def from_the_front(letter, integer):
    result = 0
    if letter.isupper():
        result = integer / (ord(letter) - 64)
    else:
        result = (ord(letter) - 96) * integer
    return result


def at_the_back(letter, current_sum):
    result = 0
    if letter.isupper():
        result = current_sum - (ord(letter) - 64)
    else:
        result = (ord(letter) - 96) + current_sum
    return result


strings = input().split()

total_sum = 0

for word in strings:
    leading_letter = word[0]
    number = int(word[1:-1])
    following_letter = word[-1]
    mid_sum = from_the_front(leading_letter, number)
    total_sum += at_the_back(following_letter, mid_sum)

print(f"{total_sum:.2f}")