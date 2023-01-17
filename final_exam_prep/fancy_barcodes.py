import re

number_of_barcodes = int(input())
pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
product_group = "00"
for _ in range(number_of_barcodes):
    barcode_to_validate = input()
    match = re.findall(pattern, barcode_to_validate)
    if not match:
        print("Invalid barcode")
    else:
        search = r"\d"
        digits = re.findall(search, match[0][1])
        if digits:
            product_group = "".join(digits)
            print(f"Product group: {product_group}")
        else:
            product_group = "00"
            print(f"Product group: {product_group}")
