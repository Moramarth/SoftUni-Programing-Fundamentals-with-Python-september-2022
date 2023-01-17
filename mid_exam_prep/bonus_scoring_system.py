from math import ceil

number_of_students = int(input())
lectures_count = int(input())
additional_bonus = int(input())

max_bonus = 0
lectures_attended = 0

for i in range(number_of_students):
    attendance = int(input())
    total_bonus = attendance / lectures_count * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        lectures_attended = attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {lectures_attended} lectures.")
