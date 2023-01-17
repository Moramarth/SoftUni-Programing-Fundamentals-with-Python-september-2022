def result_func(dictionary):
    result = ""
    for key in dictionary:
        result += f"{key} -> Mileage: {dictionary[key][0]} kms, Fuel in the tank: {dictionary[key][1]} lt.\n"
    return result


def drive_func(dictionary, car, distance, fuel):
    if fuel > dictionary[car][1]:
        print("Not enough fuel to make that ride")
    else:
        dictionary[car][0] += distance
        dictionary[car][1] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if dictionary[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del dictionary[car]


def refuel_fun(dictionary, car, fuel):
    current_fuel = dictionary[car][1]
    if current_fuel + fuel > 75:
        print(f"{car} refueled with {75 - current_fuel} liters")
        current_fuel = 75
    else:
        current_fuel += fuel
        print(f"{car} refueled with {fuel} liters")
    dictionary[car][1] = current_fuel


def revert_func(dictionary, car, kilometers):
    current_mileage = dictionary[car][0]
    if current_mileage - kilometers <= 10000:
        current_mileage = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
        current_mileage -= kilometers
    dictionary[car][0] = current_mileage


def garage_func(dictionary, cars):
    for _ in range(cars):
        car, mileage, fuel = input().split("|")
        dictionary[car] = [int(mileage), int(fuel)]


def need_for_speed(cars):
    garage = dict()
    garage_func(garage, cars)

    command = input()

    while command != "Stop":
        data = command.split(" : ")
        to_do = data[0]
        car = data[1]
        if to_do == "Drive":
            distance, fuel = int(data[2]), int(data[3])
            drive_func(garage, car, distance, fuel)
        elif to_do == "Refuel":
            fuel = int(data[2])
            refuel_fun(garage, car, fuel)
        elif to_do == "Revert":
            kilometers = int(data[2])
            revert_func(garage, car, kilometers)
        command = input()

    print(result_func(garage))


number_of_cars = int(input())
need_for_speed(number_of_cars)