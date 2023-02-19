planned_courses = input().split(", ")

command = input()

while command != "course start":
    to_do, lesson_title, *additional_info = command.split(":")

    if to_do == "Add":
        if lesson_title not in planned_courses:
            planned_courses.append(lesson_title)

    elif to_do == "Insert":
        if lesson_title not in planned_courses:
            planned_courses.insert(int(additional_info[0]), lesson_title)

    elif to_do == "Remove":

        if lesson_title in planned_courses:
            planned_courses.remove(lesson_title)
            if f"{lesson_title}-Exercise" in planned_courses:
                planned_courses.remove(f"{lesson_title}-Exercise")

    elif to_do == "Swap":
        if lesson_title and additional_info[0] in planned_courses:
            first_index = planned_courses.index(lesson_title)
            second_index = planned_courses.index(additional_info[0])

            planned_courses[first_index], planned_courses[second_index] =\
                planned_courses[second_index], planned_courses[first_index]

            if f"{lesson_title}-Exercise" in planned_courses:
                planned_courses.remove(f"{lesson_title}-Exercise")
                planned_courses.insert(planned_courses.index(lesson_title) + 1, f"{lesson_title}-Exercise")

            if f"{additional_info[0]}-Exercise" in planned_courses:
                planned_courses.remove(f"{additional_info[0]}-Exercise")
                planned_courses.insert(planned_courses.index(additional_info[0]) + 1, f"{additional_info[0]}-Exercise")

    elif to_do == "Exercise":
        if lesson_title in planned_courses and f"{lesson_title}-Exercise" not in planned_courses:
            planned_courses.insert(planned_courses.index(lesson_title) + 1, f"{lesson_title}-Exercise")
        elif lesson_title not in planned_courses:
            planned_courses.append(lesson_title)
            planned_courses.append(f"{lesson_title}-Exercise")

    command = input()


for index in range(len(planned_courses)):
    print(f"{index + 1}.{planned_courses[index]}")
