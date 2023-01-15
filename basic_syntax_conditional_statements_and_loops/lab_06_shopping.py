budget = int(input())

total_cost = 0
price = input()

while price != "End":
    cost = int(price)
    total_cost += cost
    if total_cost > budget:
        print("You went in overdraft!")
        break
    price = input()
else:
    print("You bought everything needed.")
