def winning_or_not(item):
    first_half = item[:10]
    second_half = item[10:]
    for symbol in winning_symbols:
        for repeats in range(10, 5, -1):
            needed_match = repeats * symbol
            if needed_match in first_half and needed_match in second_half:
                if repeats == 10:
                    return f'ticket "{item}" - 10{symbol} Jackpot!'
                return f'ticket "{item}" - {repeats}{symbol}'
    return f'ticket "{item}" - no match'


tickets_to_process = input().split(", ")
tickets_to_process = [ticket.strip() for ticket in tickets_to_process]

winning_symbols = ["@", "$", "#", "^"]

for ticket in tickets_to_process:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    print(winning_or_not(ticket))
