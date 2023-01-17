days_of_plunder = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())

current_plunder = 0

for day in range(1, days_of_plunder + 1):
    current_plunder += plunder_per_day

    if day % 3 == 0:
        current_plunder += 0.5 * plunder_per_day

    if day % 5 == 0:
        current_plunder -= current_plunder * 0.30

if expected_plunder <= current_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    percent = current_plunder / (expected_plunder / 100)
    print(f"Collected only {percent:.2f}% of the plunder.")
