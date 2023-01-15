booby_trap = input()

explosion_strength = 0

remaining_letters = ""

for index in range(len(booby_trap)):
    if explosion_strength > 0:
        if booby_trap[index] != ">":
            explosion_strength -= 1
            continue
    if booby_trap[index] == ">":
        remaining_letters += booby_trap[index]
        explosion_strength += int(booby_trap[index + 1])
    elif booby_trap[index] != ">":
        remaining_letters += booby_trap[index]

print(remaining_letters)
