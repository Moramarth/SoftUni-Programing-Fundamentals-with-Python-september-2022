def students_data():
    result = list()

    for key, value in user_contests.items():
        user_contests[key] = sorted(value.items(), key=lambda x: (-x[1], x[0]))
    data = sorted(user_contests.items(), key=lambda x: x[0])

    result.append("Ranking:")
    for info in data:
        intern = info[0]
        result.append(f"{intern}")
        for item in info[1]:
            contest, points = item[0], item[1]
            result.append(f"#  {contest} -> {points}")

    return "\n".join(result)


def best_candidate():
    for key, value in user_contests.items():
        user_total_points[key] = 0
        for contest, points in value.items():
            user_total_points[key] += points

    best_score = max(user_total_points.values())
    best_participant = ""

    for key, value in user_total_points.items():
        if value == best_score:
            best_participant = key
            break

    return f"Best candidate is {best_participant} with total {best_score} points."


def submission_processing():
    submission = input()

    while submission != "end of submissions":
        contest, password, username, points = submission.split("=>")
        if contest in contests_init and password == contests_init[contest]:
            if username not in user_contests:
                user_contests[username] = dict()
                user_contests[username][contest] = int(points)

            elif contest in user_contests[username]:
                if int(points) < user_contests[username][contest]:
                    points = user_contests[username][contest]
                user_contests[username][contest] = int(points)
            else:
                user_contests[username][contest] = int(points)

        submission = input()


def initial_data_store():
    contest_command = input()

    while contest_command != "end of contests":
        contest, password = contest_command.split(":")
        contests_init[contest] = password

        contest_command = input()


contests_init = dict()
user_total_points = dict()
user_contests = dict()

initial_data_store()
submission_processing()
print(best_candidate())
print(students_data())
