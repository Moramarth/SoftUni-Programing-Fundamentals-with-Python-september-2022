people_to_die = input().split(" ")

next_in_line = int(input())

order_of_execution = list()
count = 0
index = 0
while len(people_to_die) >= 1:
    count += 1
    if count % next_in_line == 0:
        dead = people_to_die[index]
        people_to_die.pop(index)
        order_of_execution.append(dead)
    else:
        index += 1

    if index >= len(people_to_die):
        index = 0
string = ",".join(order_of_execution)

print(f"[{string}]")
