vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

text = input()

no_vowels = [letter for letter in text if letter not in vowels]

print("".join(no_vowels))
