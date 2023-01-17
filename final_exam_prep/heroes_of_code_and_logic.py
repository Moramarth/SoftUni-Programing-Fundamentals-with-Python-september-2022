def game_over(dictionary):
    ending = ""
    for key in dictionary:
        ending += f"{key}\n  HP: {dictionary[key][0]}\n  MP: {dictionary[key][1]}\n"
    return ending


def heal(dictionary, hero, bonus_hp):
    current_hp = dictionary[hero][0]
    if current_hp + bonus_hp >= 100:
        print(f"{hero} healed for {100 - current_hp} HP!")
        current_hp = 100
    else:
        current_hp += bonus_hp
        print(f"{hero} healed for {bonus_hp} HP!")
    dictionary[hero][0] = current_hp


def recharge(dictionary, hero, bonus_mp):
    current_mana = dictionary[hero][1]
    if current_mana + bonus_mp >= 200:
        print(f"{hero} recharged for {200 - current_mana} MP!")
        current_mana = 200
    else:
        current_mana += bonus_mp
        print(f"{hero} recharged for {bonus_mp} MP!")
    dictionary[hero][1] = current_mana


def take_damage(dictionary, hero, damage, attacker):
    current_hp = dictionary[hero][0]
    if current_hp <= damage:
        print(f"{hero} has been killed by {attacker}!")
        del dictionary[hero]
    else:
        current_hp -= damage
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        dictionary[hero][0] = current_hp


def cast_a_spell(dictionary, hero, mp_needed, spell_name):
    current_mana = dictionary[hero][1]
    if current_mana < mp_needed:
        print(f"{hero} does not have enough MP to cast {spell_name}!")
    else:
        current_mana -= mp_needed
        print(f"{hero} has successfully cast {spell_name} and now has {current_mana} MP!")
    dictionary[hero][1] = current_mana


def create_characters_func(dictionary, integer):
    for _ in range(integer):
        data = input().split()
        character, hp, mp = data[0], int(data[1]), int(data[2])
        dictionary[character] = [hp, mp]


def gameplay(integer):
    characters = dict()
    create_characters_func(characters, integer)

    command = input()

    while command != "End":
        data = command. split(" - ")
        to_do, hero = data[0], data[1]
        if to_do == "CastSpell":
            mp_needed, spell_name = int(data[2]), data[3]
            cast_a_spell(characters, hero, mp_needed, spell_name)
        elif to_do == "TakeDamage":
            damage, attacker = int(data[2]), data[3]
            take_damage(characters, hero, damage, attacker)
        elif to_do == "Recharge":
            bonus_mp = int(data[2])
            recharge(characters, hero, bonus_mp)
        elif to_do == "Heal":
            bonus_hp = int(data[2])
            heal(characters, hero, bonus_hp)

        command = input()

    print(game_over(characters))


number_of_heroes = int(input())
gameplay(number_of_heroes)
