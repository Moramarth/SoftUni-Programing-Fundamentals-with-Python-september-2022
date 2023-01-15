player_cards = input().split(" ")

sent_off = list()

team_a_count = 11
team_b_count = 11
condition = False
for element in player_cards:
    if element not in sent_off:
        sent_off.append(element)
        if "A" in element:
            team_a_count -= 1
        else:
            team_b_count -= 1
        if team_a_count < 7 or team_b_count < 7:
            condition = True
            break

print(f"Team A - {team_a_count}; Team B - {team_b_count}")
if condition:
    print("Game was terminated")
