students = dict()

grades_count = int(input())

for grades in range(grades_count):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = [grade]
    else:
        students[student_name].append(grade)

dropped_students = {key for key in students if (sum(students[key])/len(students[key]) < 4.50)}
for student in dropped_students:
    if student in students:
        students.pop(student)

for key in students:
    average_grade = sum(students[key])/len(students[key])
    print(f"{key} -> {average_grade:.2f}")
