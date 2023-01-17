def result_func(dictionary, total):
    result = ""
    for key in dictionary:
        result += f"{key}: {dictionary[key]}\n"
    result += f"All sold: {total} goods"
    return result


def receive_func(dictionary, number, food_type):
    if number > 0:
        if food_type not in dictionary:
            dictionary[food_type] = number
        else:
            dictionary[food_type] += number


def sell_func(dictionary, number, food_type):
    if food_type not in dictionary:
        print(f"You do not have any {food_type}.")
        sold = 0
    elif number > dictionary[food_type]:
        print(f"There aren't enough {food_type}. You sold the last {dictionary[food_type]} of them.")
        sold = dictionary[food_type]
        del dictionary[food_type]

    else:
        dictionary[food_type] -= number
        sold = number
        print(f"You sold {number} {food_type}.")
        if dictionary[food_type] == 0:
            del dictionary[food_type]
    return sold


command = input()

stock = dict()
goods_sold = 0

while command != "Complete":
    data = command.split()
    to_do, quantity, food = data[0], int(data[1]), data[2]
    if to_do == "Receive":
        receive_func(stock, quantity, food)
    elif to_do == "Sell":
        goods_sold += sell_func(stock, quantity, food)

    command = input()

print(result_func(stock, goods_sold))