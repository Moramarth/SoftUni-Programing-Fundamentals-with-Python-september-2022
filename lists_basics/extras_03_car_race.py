race_track = input().split(" ")

mid_index = len(race_track) // 2

left_track = race_track[:mid_index]
right_track = race_track[mid_index + 1:]
right_track = list(reversed(right_track))
left_time = 0
right_time = 0

for step in left_track:
    if int(step) != 0:
        left_time += int(step)
    else:
        left_time -= 0.20 * left_time

for step in right_track:
    if int(step) != 0:
        right_time += int(step)
    else:
        right_time -= 0.20 * right_time

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")
