def evens(number):
    if number % 2 != 0:
        return False
    else:
        return True


numbers = input().split(" ")

integers = list(map(int, numbers))

evens_list = list(filter(evens, integers))

print(evens_list)
