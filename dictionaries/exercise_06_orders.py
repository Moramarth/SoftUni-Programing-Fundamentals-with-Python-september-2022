shopping_cart = dict()

while True:
    data = input().split()
    if len(data) == 1:
        break
    product = data[0]
    price = float(data[1])
    quantity = int(data[2])

    if product not in shopping_cart:
        shopping_cart[product] = [price, quantity]
    else:
        shopping_cart[product][0] = price
        shopping_cart[product][1] += quantity

for key in shopping_cart:
    print(f"{key} -> {shopping_cart[key][0] * shopping_cart[key][1]:.2f}")
