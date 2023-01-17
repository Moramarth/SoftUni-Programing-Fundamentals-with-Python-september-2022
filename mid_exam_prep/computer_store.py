extra_discount = False
no_tax_price = 0
while True:
    command = input()
    if command == "special" or command == "regular":
        if command == "special":
            extra_discount = True
        break
    price = float(command)
    if price >= 0:
        no_tax_price += price
    else:
        print("Invalid price!")

taxes = no_tax_price * 0.20
final_price = no_tax_price + taxes
if extra_discount:
    final_price -= 0.10 * final_price
if final_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {no_tax_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")
