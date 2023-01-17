import re

random_string = input()
pattern = r"(#|\|)([A-Za-z]+[ A-Za-z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"

result = re.findall(pattern, random_string)

total_calories = 0
item_information = ""
for item in result:
    item_information += f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}\n"
    total_calories += int(item[3])

days = int(total_calories / 2000)
print(f"You have food to last you for: {days} days!")
if item_information:
    print(item_information)
