original_deck_of_cards = input().split(" ")
deck_shuffles = int(input())

deck_first_half = original_deck_of_cards[:len(original_deck_of_cards)//2]
deck_second_half = original_deck_of_cards[len(original_deck_of_cards)//2:]

current_deck = list()
for i in range(deck_shuffles):
    current_deck.clear()
    for j in range(len(deck_first_half)):
        current_deck.append(deck_first_half[j])
        current_deck.append(deck_second_half[j])
    deck_first_half = current_deck[:len(current_deck) // 2]
    deck_second_half = current_deck[len(current_deck) // 2:]


print(current_deck)
