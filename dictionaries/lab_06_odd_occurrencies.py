words = input().lower().split()

odds = dict()

for word in words:
    if words.count(word) % 2 != 0:
        odds[word] = words.count(word)

print(" ".join(odds.keys()))
