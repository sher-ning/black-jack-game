from random import *


class GameDeck:

    def __init__(self) -> None:
        self.deck = self.new_deck()

    def new_deck(self):
        deck = []
        for i in range(1, 14):
            for x in range(4):
                deck.append(i)
        return deck

    def draw_card(self):
        for _ in range(len(self.deck)):
            position = randint(0, 51)
            card = self.deck[position]
            if card == -1:
                continue

            self.deck[position] = -1
            return card
