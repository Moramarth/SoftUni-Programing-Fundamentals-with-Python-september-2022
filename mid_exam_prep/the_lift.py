people_waiting = int(input())
lift_state = input().split(" ")
available_seats = list(map(int, lift_state))


for i in range(len(available_seats)):
    if available_seats[i] < 4:
        difference = 4 - available_seats[i]
        if people_waiting < difference:
            available_seats[i] += people_waiting
        else:
            available_seats[i] = 4
        people_waiting -= difference
        if people_waiting <= 0:
            break

final_lift_state = [str(wagon) for wagon in available_seats]
are_all_seats_taken = [seat for seat in available_seats if seat != 4]

if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
elif len(are_all_seats_taken) > 0:
    print(f"The lift has empty spots!")

print(f"{' '.join(final_lift_state)}")
