from math import ceil
budget = float(input())
students = int(input())
flour_price = float(input())
one_egg_price = float(input())
single_apron = float(input())

total_eggs = students * one_egg_price * 10
free_packs = students // 5

total_flour = (students - free_packs) * flour_price
total_apron = ceil(students * 1.20) * single_apron

total_cost = total_flour + total_apron + total_eggs

difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    print(f"{difference:.2f}$ more needed.")
