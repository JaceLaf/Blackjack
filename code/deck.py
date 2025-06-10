from card import Card
import random

class Deck:

    # Initialization function
    def __init__(self):
        self.deck = []

        # Creates a list of the ASCII graphics for the card
        graphics = [
            "|---------|\n| A       |\n|         |\n|    ♠    |\n|         |\n|       A |\n|---------|\n",
            "|---------|\n| 2       |\n|         |\n|    ♠    |\n|         |\n|       2 |\n|---------|\n",
            "|---------|\n| 3       |\n|         |\n|    ♠    |\n|         |\n|       3 |\n|---------|\n",
            "|---------|\n| 4       |\n|         |\n|    ♠    |\n|         |\n|       4 |\n|---------|\n",
            "|---------|\n| 5       |\n|         |\n|    ♠    |\n|         |\n|       5 |\n|---------|\n",
            "|---------|\n| 6       |\n|         |\n|    ♠    |\n|         |\n|       6 |\n|---------|\n",
            "|---------|\n| 7       |\n|         |\n|    ♠    |\n|         |\n|       7 |\n|---------|\n",
            "|---------|\n| 8       |\n|         |\n|    ♠    |\n|         |\n|       8 |\n|---------|\n",
            "|---------|\n| 9       |\n|         |\n|    ♠    |\n|         |\n|       9 |\n|---------|\n",
            "|---------|\n| 10      |\n|         |\n|    ♠    |\n|         |\n|      10 |\n|---------|\n",
            "|---------|\n| J       |\n|         |\n|    ♠    |\n|         |\n|       J |\n|---------|\n",
            "|---------|\n| Q       |\n|         |\n|    ♠    |\n|         |\n|       Q |\n|---------|\n",
            "|---------|\n| K       |\n|         |\n|    ♠    |\n|         |\n|       K |\n|---------|\n",
            
            "|---------|\n| A       |\n|         |\n|    ♣    |\n|         |\n|       A |\n|---------|\n",
            "|---------|\n| 2       |\n|         |\n|    ♣    |\n|         |\n|       2 |\n|---------|\n",
            "|---------|\n| 3       |\n|         |\n|    ♣    |\n|         |\n|       3 |\n|---------|\n",
            "|---------|\n| 4       |\n|         |\n|    ♣    |\n|         |\n|       4 |\n|---------|\n",
            "|---------|\n| 5       |\n|         |\n|    ♣    |\n|         |\n|       5 |\n|---------|\n",
            "|---------|\n| 6       |\n|         |\n|    ♣    |\n|         |\n|       6 |\n|---------|\n",
            "|---------|\n| 7       |\n|         |\n|    ♣    |\n|         |\n|       7 |\n|---------|\n",
            "|---------|\n| 8       |\n|         |\n|    ♣    |\n|         |\n|       8 |\n|---------|\n",
            "|---------|\n| 9       |\n|         |\n|    ♣    |\n|         |\n|       9 |\n|---------|\n",
            "|---------|\n| 10      |\n|         |\n|    ♣    |\n|         |\n|      10 |\n|---------|\n",
            "|---------|\n| J       |\n|         |\n|    ♣    |\n|         |\n|       J |\n|---------|\n",
            "|---------|\n| Q       |\n|         |\n|    ♣    |\n|         |\n|       Q |\n|---------|\n",
            "|---------|\n| K       |\n|         |\n|    ♣    |\n|         |\n|       K |\n|---------|\n",

            "|---------|\n| A       |\n|         |\n|    ♥    |\n|         |\n|       A |\n|---------|\n",
            "|---------|\n| 2       |\n|         |\n|    ♥    |\n|         |\n|       2 |\n|---------|\n",
            "|---------|\n| 3       |\n|         |\n|    ♥    |\n|         |\n|       3 |\n|---------|\n",
            "|---------|\n| 4       |\n|         |\n|    ♥    |\n|         |\n|       4 |\n|---------|\n",
            "|---------|\n| 5       |\n|         |\n|    ♥    |\n|         |\n|       5 |\n|---------|\n",
            "|---------|\n| 6       |\n|         |\n|    ♥    |\n|         |\n|       6 |\n|---------|\n",
            "|---------|\n| 7       |\n|         |\n|    ♥    |\n|         |\n|       7 |\n|---------|\n",
            "|---------|\n| 8       |\n|         |\n|    ♥    |\n|         |\n|       8 |\n|---------|\n",
            "|---------|\n| 9       |\n|         |\n|    ♥    |\n|         |\n|       9 |\n|---------|\n",
            "|---------|\n| 10      |\n|         |\n|    ♥    |\n|         |\n|      10 |\n|---------|\n",
            "|---------|\n| J       |\n|         |\n|    ♥    |\n|         |\n|       J |\n|---------|\n",
            "|---------|\n| Q       |\n|         |\n|    ♥    |\n|         |\n|       Q |\n|---------|\n",
            "|---------|\n| K       |\n|         |\n|    ♥    |\n|         |\n|       K |\n|---------|\n",

            "|---------|\n| A       |\n|         |\n|    ♦    |\n|         |\n|       A |\n|---------|\n",
            "|---------|\n| 2       |\n|         |\n|    ♦    |\n|         |\n|       2 |\n|---------|\n",
            "|---------|\n| 3       |\n|         |\n|    ♦    |\n|         |\n|       3 |\n|---------|\n",
            "|---------|\n| 4       |\n|         |\n|    ♦    |\n|         |\n|       4 |\n|---------|\n",
            "|---------|\n| 5       |\n|         |\n|    ♦    |\n|         |\n|       5 |\n|---------|\n",
            "|---------|\n| 6       |\n|         |\n|    ♦    |\n|         |\n|       6 |\n|---------|\n",
            "|---------|\n| 7       |\n|         |\n|    ♦    |\n|         |\n|       7 |\n|---------|\n",
            "|---------|\n| 8       |\n|         |\n|    ♦    |\n|         |\n|       8 |\n|---------|\n",
            "|---------|\n| 9       |\n|         |\n|    ♦    |\n|         |\n|       9 |\n|---------|\n",
            "|---------|\n| 10      |\n|         |\n|    ♦    |\n|         |\n|      10 |\n|---------|\n",
            "|---------|\n| J       |\n|         |\n|    ♦    |\n|         |\n|       J |\n|---------|\n",
            "|---------|\n| Q       |\n|         |\n|    ♦    |\n|         |\n|       Q |\n|---------|\n",
            "|---------|\n| K       |\n|         |\n|    ♦    |\n|         |\n|       K |\n|---------|\n"
        ]

        # Creates lists of other needed variables
        suits = ["spades", "clubs", "hearts", "diamonds"]
        titles = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
        values = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        # Iterates through each graphic and generates a matching card object
        index = 0
        for suit in suits:
            for value, title in zip(values, titles):
                name = title + ' of ' + suit
                card = Card(name, value, suit, graphics[index])
                index += 1
                self.deck.append(card)
        
        # Creates a preserved copy of the original deck
        self.original_deck = self.deck

        # Creates a list of the cards that have been discarded
        self.cards_out = []
        self.discards = []

    # Shuffles the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # Shuffles discards
    def shuffle_discards(self):
        random.shuffle(self.discards)

    # Draws a card from the top
    def draw(self):
        # Checks if there are no cards left and reshuffles the discards
        if not self.deck:
            if not self.discards:
                raise IndexError("No cards in discard pile or deck.")
            self.deck = self.shuffle_discards()
        
        top_card = self.deck.pop(0)

        return top_card
    
    # Deals out cards given a number of cards per player and number of players
    def deal(self, num_players = 1, num_cards = 1):
        cards_dealt = [[] for i in range(num_players)]

        # Draws a card in the order of players for each set
        for i in range(num_cards):
            for j in range(num_players):
                card = self.draw()
                cards_dealt[j].append(card)
        
        return cards_dealt