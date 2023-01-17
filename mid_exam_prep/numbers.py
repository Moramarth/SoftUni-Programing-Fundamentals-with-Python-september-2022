data = input().split()

integer_list = list(map(int, data))

average = sum(integer_list) / len(integer_list)

top_five = [integer for integer in integer_list if integer > average]

if not top_five:
    print("No")
elif len(top_five) > 5:
    top_five.sort()
    top_five.reverse()
    top_five = top_five[:5]
    data = [str(integer) for integer in top_five]
    print(" ".join(data))
else:
    top_five.sort()
    top_five.reverse()
    data = [str(integer) for integer in top_five]
    print(" ".join(data))
