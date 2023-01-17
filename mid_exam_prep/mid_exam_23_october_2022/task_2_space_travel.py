travel_route = input().split("||")
fuel_amount = int(input())
ammunition = int(input())

for i in range(len(travel_route)):
    if travel_route[i] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    surprise, value = travel_route[i].split()
    if surprise == "Travel":
        light_years = int(value)
        if fuel_amount >= light_years:
            fuel_amount -= light_years
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print("Mission failed.")
            break
    elif surprise == "Enemy":
        armour = int(value)
        if ammunition >= armour:
            ammunition -= armour
            print(f"An enemy with {armour} armour is defeated.")
        else:
            if fuel_amount >= 2 * armour:
                fuel_amount -= 2 * armour
                print(f"An enemy with {armour} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif surprise == "Repair":
        stock = int(value)
        ammunition += 2 * stock
        print(f"Ammunitions added: {2 * stock}.")
        fuel_amount += stock
        print(f"Fuel added: {stock}.")
