deck_of_cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    for index_of_the_card in range(len(left_part)):
        final_deck.append(left_part[index_of_the_card])
        final_deck.append(right_part[index_of_the_card])
    deck_of_cards = final_deck

print(deck_of_cards)
