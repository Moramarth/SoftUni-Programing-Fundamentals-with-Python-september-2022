types_of_fire = input().split("#")
water_volume = int(input())

effort = 0
total_fire = 0
valid_fire = False

print("Cells:")

for fire in types_of_fire:
    variables = fire.split(" = ")
    fire_type = variables[0]
    fire_intensity = int(variables[1])
    valid_fire = False

    if fire_type == "High":
        if 80 < fire_intensity < 126:
            valid_fire = True
    elif fire_type == "Medium":
        if 50 < fire_intensity < 81:
            valid_fire = True
    elif fire_type == "Low":
        if 0 < fire_intensity < 51:
            valid_fire = True

    if valid_fire:
        if water_volume >= fire_intensity:
            effort += 0.25 * fire_intensity
            water_volume -= fire_intensity
            print(f" - {fire_intensity}")
            total_fire += fire_intensity

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
