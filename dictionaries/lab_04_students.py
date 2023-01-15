keyword = ""
students = dict()

while True:
    command = input()
    info = command.split(":")
    if len(info) == 1:
        keyword = info[0]
        break

    name = info[0]
    unique_id = info[1]
    course = info[2].replace(" ", "_").lower()

    students[unique_id] = {name: course}


for key, value in students.items():
    for name, course in value.items():
        if course == keyword:
            print(f"{name} - {key}")
