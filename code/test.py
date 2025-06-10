from card import Card
from deck import Deck

if __name__ == "__main__":
    d1 = Deck()
    d1.shuffle()

    hands = d1.deal(2, 7)

    for n, hand in enumerate(hands):
        print("Player", n+1)
        for card in hand:
            print(card)
            print()