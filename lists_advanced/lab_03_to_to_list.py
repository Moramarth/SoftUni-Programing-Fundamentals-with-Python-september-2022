notes = ["0" for num in range(11)]

new_to_do = input()

while new_to_do != "End":
    task = new_to_do.split("-")
    index = int(task[0])
    notes[index] = task[1]

    new_to_do = input()

notes = [to_do for to_do in notes if to_do != "0"]
print(notes)
