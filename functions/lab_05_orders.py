def calculation(order_type, amount):
    if order_type == "coffee":
        price = 1.50 * amount
    elif order_type == "coke":
        price = 1.40 * amount
    elif order_type == "water":
        price = amount
    elif order_type == "snacks":
        price = 2 * amount
    return price


orders = input()
quantity = int(input())
result = calculation(orders, quantity)
print(f"{result:.2f}")
