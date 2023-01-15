number_of_rooms = int(input())

enough_chairs = True
seats_taken = 0
total_chairs = 0
room_number = 0
for i in range(number_of_rooms):
    room_number += 1
    chairs, visitors = input().split()

    if len(chairs) < int(visitors):
        print(f"{int(visitors) - len(chairs)} more chairs needed in room {room_number}")
        enough_chairs = False
    else:
        seats_taken += int(visitors)
        total_chairs += len(chairs)

if enough_chairs:
    print(f"Game On, {total_chairs - seats_taken} free chairs left")
