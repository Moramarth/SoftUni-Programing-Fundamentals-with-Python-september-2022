text_to_process = input()

for i in range(len(text_to_process)):
    if text_to_process[i] == ":":
        print(text_to_process[i] + text_to_process[i+1])
