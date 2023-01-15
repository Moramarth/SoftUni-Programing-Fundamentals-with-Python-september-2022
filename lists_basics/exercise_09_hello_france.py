item_collection = input().split("|")
budget = float(input())

new_prices_list = list()
prices_strings = list()
profit = 0
total_money = 0
price_is_right = False

for position in item_collection:
    variables = position.split("->")
    item = variables[0]
    price = float(variables[1])
    price_is_right = False

    if item == "Clothes":
        if price <= 50:
            price_is_right = True
    elif item == "Shoes":
        if price <= 35:
            price_is_right = True
    elif item == "Accessories":
        if price <= 20.50:
            price_is_right = True

    if price_is_right:
        if price <= budget:
            budget -= price
            current_price = 1.40 * price
            profit += current_price - price
            new_prices_list.append(current_price)
            prices_strings.append(f"{current_price:.2f}")

print(" ".join(prices_strings))
print(f"Profit: {profit:.2f}")

if budget + sum(new_prices_list) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
