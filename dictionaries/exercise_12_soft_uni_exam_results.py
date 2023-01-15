statistics = {"results": {}, "languages": {}}

data = input()

while data != "exam finished":
    if "banned" in data:
        username = data.split("-")[0]
        statistics["results"].pop(username)
    else:
        username, language, points = data.split("-")
        if username not in statistics["results"]:
            statistics["results"][username] = int(points)
        else:
            if statistics["results"][username] < int(points):
                statistics["results"][username] = int(points)

        if language not in statistics["languages"]:
            statistics["languages"][language] = 1
        else:
            statistics["languages"][language] += 1
    data = input()

print("Results:")
for key, value in statistics["results"].items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in statistics["languages"].items():
    print(f"{key} - {value}")
