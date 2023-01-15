work_days_events = input().split("|")

energy = 100
coins = 100
day_success = True

for event in work_days_events:
    variables = event.split("-")
    command = variables[0]
    value = int(variables[1])
    if command == "rest":
        gain = value
        current_energy = energy + gain
        if current_energy >= 100:
            current_energy = 100
        print(f"You gained {current_energy - energy} energy.")
        energy = current_energy
        print(f"Current energy: {energy}.")

    elif command == "order":
        if energy >= 30:
            coins += value
            print(f"You earned {value} coins.")
            energy -= 30
        else:
            print("You had to rest!")
            energy += 50
    else:
        if coins >= value:
            print(f"You bought {command}.")
            coins -= value
        else:
            print(f"Closed! Cannot afford {command}.")
            day_success = False
            break

if day_success:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
