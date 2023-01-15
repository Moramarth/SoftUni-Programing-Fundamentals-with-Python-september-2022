number_of_people = int(input())
elevator_capacity = int(input())

full_capacity_courses = number_of_people // elevator_capacity
if number_of_people % elevator_capacity != 0:
    full_capacity_courses += 1

print(full_capacity_courses)
