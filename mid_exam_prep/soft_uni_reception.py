first_employee_efficiency_per_hour = int(input())
second_employee_efficiency_per_hour = int(input())
third_employee_efficiency_per_hour = int(input())

students_to_assist = int(input())

hours_passed = 0

while students_to_assist > 0:
    hours_passed += 1
    if hours_passed % 4 == 0:
        continue
    assisted_students = first_employee_efficiency_per_hour + second_employee_efficiency_per_hour + \
                        third_employee_efficiency_per_hour
    students_to_assist -= assisted_students

print(f"Time needed: {hours_passed}h.")
