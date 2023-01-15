number_list = input().split(", ")

no_zero_list = [number for number in number_list if number != "0"]
zero_list = [number for number in number_list if number == "0"]
no_zero_list.extend(zero_list)
final_list = list(map(int, no_zero_list))

print(final_list)
