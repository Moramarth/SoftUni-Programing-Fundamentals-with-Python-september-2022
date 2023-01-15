factor = int(input())
number_of_multiplications = int(input())

result_list = list()

for i in range(1, number_of_multiplications + 1):
    current_result = i * factor
    result_list.append(current_result)

print(result_list)
