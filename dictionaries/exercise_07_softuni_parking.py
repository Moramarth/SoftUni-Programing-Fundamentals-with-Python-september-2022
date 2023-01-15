registration_count = int(input())

parking_lot = dict()

for parking_users in range(registration_count):
    attempt = input().split()
    if attempt[0] == "register":
        username = attempt[1]
        licence_plate = attempt[2]
        if username not in parking_lot.keys():
            parking_lot[username] = licence_plate
            print(f"{username} registered {licence_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
    elif attempt[0] == "unregister":
        username = attempt[1]
        if username not in parking_lot.keys():
            print(f"ERROR: user {username} not found")
        else:
            parking_lot.pop(username)
            print(f"{username} unregistered successfully")

for key in parking_lot:
    print(f"{key} => {parking_lot[key]}")
