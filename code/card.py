class Card:

    # Initialization function
    def __init__(self, name, value, suit, graphic):
        self.name = name
        self.value = value
        self.suit = suit
        self.graphic = graphic

    # Prints out a card
    def __str__(self):
        print(self.graphic)