words_count = int(input())

my_dict = dict()

for _ in range(words_count):
    word = input()
    synonym = input()
    if word not in my_dict:
        my_dict[word] = [synonym]
    else:
        my_dict[word].append(synonym)

for key in my_dict:
    print(f"{key} - {', '.join(my_dict[key])}")
