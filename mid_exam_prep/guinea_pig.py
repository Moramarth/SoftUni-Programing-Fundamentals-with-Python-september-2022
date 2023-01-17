food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
guinea_weight = float(input()) * 1000

for day in range(1, 31):
    food_quantity -= 300

    if day % 2 == 0:
        hay_quantity -= food_quantity * 0.05

    if day % 3 == 0:
        cover_quantity -= guinea_weight / 3
    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        print("Merry must go to the pet store!")
        break

else:
    food_quantity = food_quantity / 1000
    hay_quantity = hay_quantity / 1000
    cover_quantity = cover_quantity / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity:.2f}, "
          f"Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")
