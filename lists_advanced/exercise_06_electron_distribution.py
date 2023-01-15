electrons = int(input())

shells = list()
shells_count = 1
while electrons > 0:
    if electrons > 2*(shells_count**2):
        electrons -= 2*(shells_count**2)
        shells.append(2*(shells_count**2))
    else:
        shells.append(electrons)
        electrons = 0
    shells_count += 1
print(shells)
