def join_side(side, candidate):
    if not the_force:
        the_force[side] = [candidate]
        return the_force
    does_not_exist = True
    for key in the_force:
        for value in the_force[key]:
            if value == candidate:
                does_not_exist = False
    if does_not_exist and side not in the_force:
        the_force[side] = [candidate]
    elif does_not_exist:
        the_force[side].append(candidate)


def switch_side(side, candidate):
    special_announcement = False
    for key, value in the_force.items():
        if candidate in value:
            the_force[key].pop(value.index(candidate))
            break
    if side not in the_force:
        the_force[side] = [candidate]
        special_announcement = True
    else:
        the_force[side].append(candidate)
        special_announcement = True

    return special_announcement


the_force = dict()

command = input()

while command != "Lumpawaroo":
    if "|" in command:
        data = command.split(" | ")
        force_side = data[0]
        user = data[1]
        join_side(force_side, user)
    elif "->" in command:
        data = command.split(" -> ")
        user = data[0]
        force_side = data[1]
        condition = switch_side(force_side, user)
        if condition:
            print(f"{user} joins the {force_side} side!")

    command = input()

to_remove = []
for key_word in the_force:
    if not the_force[key_word]:
        to_remove.append(key_word)

for key_word in to_remove:
    if key_word in the_force:
        the_force.pop(key_word)

for key_word in the_force:
    print(f"Side: {key_word}, Members: {len(the_force[key_word])}")
    for needed_value in the_force[key_word]:
        print(f"! {needed_value}")
