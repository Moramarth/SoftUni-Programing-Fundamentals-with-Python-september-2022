def add_func(dictionary, piece, composer, key):
    if piece in dictionary:
        print(f"{piece} is already in the collection!")
    else:
        dictionary[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")


def remove_func(dictionary, piece):
    if piece in dictionary:
        print(f"Successfully removed {piece}!")
        del dictionary[piece]
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key_func(dictionary, piece, key):
    if piece in dictionary:
        dictionary[piece][1] = key
        print(f"Changed the key of {piece} to {key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def result_func(dictionary):
    result = ""
    for piece in dictionary:
        result += f"{piece} -> Composer: {dictionary[piece][0]}, Key: {dictionary[piece][1]}\n"
    return result


def main_func(number):
    pieces_dictionary = dict()

    for _ in range(number):
        piece, composer, key = input().split("|")
        pieces_dictionary[piece] = [composer, key]
    command = input()
    while command != "Stop":
        data = command.split("|")
        to_do = data[0]
        new_piece = data[1]
        if to_do == "Add":
            composer, key = data[2], data[3]
            add_func(pieces_dictionary, new_piece, composer, key)
        elif to_do == "Remove":
            remove_func(pieces_dictionary, new_piece)
        elif to_do == "ChangeKey":
            key = data[2]
            change_key_func(pieces_dictionary, new_piece, key)
        command = input()

    print(result_func(pieces_dictionary))


number_of_pieces = int(input())
main_func(number_of_pieces)
