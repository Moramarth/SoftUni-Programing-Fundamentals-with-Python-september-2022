budget = float(input())
price_for_1kg_flour = float(input())

bread_count = 0
colored_eggs = 0
current_price = 0


eggs_price = 0.75 * price_for_1kg_flour
milk_price = 1.25 * price_for_1kg_flour

while True:
    current_price += milk_price / 4
    current_price += eggs_price + price_for_1kg_flour
    if current_price >= budget:
        break
    budget -= current_price
    current_price = 0
    bread_count += 1
    colored_eggs += 3
    if bread_count % 3 == 0:
        colored_eggs -= bread_count - 2

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
