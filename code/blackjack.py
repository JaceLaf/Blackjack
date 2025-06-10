from card import Card
from deck import Deck

class Blackjack:

    # Initializes class
    def __init__(self, num_real_players = 1, num_computer_players = 1):
        self.num_players = num_real_players + num_computer_players