words = input().split(" ")

palindrome = input()

all_that_are_found = list()

for word in words:
    if word == "".join(reversed(word)):
        all_that_are_found.append(word)

print(all_that_are_found)
print(f"Found palindrome {all_that_are_found.count(palindrome)} times")
