courses = dict()

while True:
    command = input().split(" : ")
    if len(command) == 1:
        break
    course_name = command[0]
    student_name = command[1]

    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)

for key in courses:
    print(f"{key}: {len(courses[key])}")
    for student in courses[key]:
        print(f"-- {student}")
