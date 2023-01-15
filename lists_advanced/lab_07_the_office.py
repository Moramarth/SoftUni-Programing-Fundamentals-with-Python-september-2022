happiness = list(map(int, input().split(" ")))

average = sum(happiness) / len(happiness)

happy_people = [person for person in happiness if person > average]

if len(happy_people) >= len(happiness) / 2:
    print(f"Score: {len(happy_people)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_people)}/{len(happiness)}. Employees are not happy!")
