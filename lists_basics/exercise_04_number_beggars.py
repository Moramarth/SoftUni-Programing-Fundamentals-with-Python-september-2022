list_of_integers = input().split(", ")

beggars_count = int(input())
beggars_to_get_integer = beggars_count

current_beggar_string = list()
current_beggar_ints = list()
current_index = list()
beggars_total = list()


while len(list_of_integers) > 0:
    for i in range(0, len(list_of_integers), beggars_to_get_integer):
        current_beggar_string.append(list_of_integers[i])
        current_beggar_ints.append(int(list_of_integers[i]))
        current_index.append(i)
    beggars_total.append(sum(current_beggar_ints))
    current_index.sort(reverse=True)
    for i in current_index:
        list_of_integers.pop(i)

    current_beggar_string = list()
    current_beggar_ints = list()
    current_index = list()

    beggars_to_get_integer -= 1
if len(beggars_total) != beggars_count:
    for _ in range(beggars_count - len(beggars_total)):
        beggars_total.append(0)

print(beggars_total)
