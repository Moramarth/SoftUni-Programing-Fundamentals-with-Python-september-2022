dungeon = input().split("|")

health = 100
bitcoins = 0
rooms_entered = 0
you_are_alive = True

for i in range(len(dungeon)):
    rooms_entered += 1
    surprise, value = dungeon[i].split()
    if surprise == "potion":
        bonus_hp = int(value)
        if bonus_hp + health > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for {bonus_hp} hp.")
            health += bonus_hp
            print(f"Current health: {health} hp.")
    elif surprise == "chest":
        bitcoin_amount = int(value)
        print(f"You found {bitcoin_amount} bitcoins.")
        bitcoins += bitcoin_amount
    else:
        attack = int(value)
        health -= attack
        if health <= 0:
            print(f"You died! Killed by {surprise}.")
            print(f"Best room: {rooms_entered}")
            you_are_alive = False
            break
        else:
            print(f"You slayed {surprise}.")

if you_are_alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
