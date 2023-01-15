ending = int(input())

current_list = [1, 1, 2, 4]
if ending < len(current_list):
    while ending < len(current_list):
        current_list.pop()
index = 4

while len(current_list) != ending:
    current_sum = current_list[index - 1] + current_list[index - 2] + current_list[index - 3]
    current_list.append(current_sum)
    index += 1

current_list = list(map(str, current_list))
print(" ".join(current_list))


# def tribonacci(number):
#     if number == 1 or number == 2:
#         return 1
#     elif number == 3:
#         return 2
#     else:
#         return tribonacci(number - 1) + tribonacci(number - 2) + tribonacci(number - 3)
#
#
# for i in range(1, ending + 1):
#     print(tribonacci(i),"", end="")
