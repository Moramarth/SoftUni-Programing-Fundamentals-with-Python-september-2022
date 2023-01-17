cryptic_message = input()

command = input()

while command != "Decode":
    orders = command.split("|")
    if orders[0] == "Move":
        number_of_letters = int(orders[1])
        cryptic_message = cryptic_message[number_of_letters:] + cryptic_message[:number_of_letters]
    elif orders[0] == "Insert":
        index, value = int(orders[1]), orders[2]
        cryptic_message = cryptic_message[:index] + value + cryptic_message[index:]
    elif orders[0] == "ChangeAll":
        substring, replacement = orders[1], orders[2]
        cryptic_message = cryptic_message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {cryptic_message}")
