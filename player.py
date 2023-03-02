
class Player:

    def __init__(self, name: str, balance: int) -> None:
        self.score = 0
        self.cards = []
        self.balance = balance
        self.name = name

    def reset(self):
        self.score = 0
        self.cards = []

    def has_black_jack(self):
        if len(self.cards) == 2 and sum(self.cards) >= 11 and 1 in self.cards:
            return True

        return False

    def has_double_ace(self):
        if len(self.cards) == 2 and sum(self.cards) < 3 and 1 in self.cards:
            return True

        return False

    def calculate_score(self):
        score = 0

        if len(self.cards) == 2 and 1 in self.cards:
            for card in self.cards:
                if card == 1:
                    score += 11
                else:
                    score += card
            
            self.score = score
            return

        else:
            for card in self.cards:
                if card > 10 or card == 1:
                    card = 10
                score += card

            if score > 21 and 1 in self.cards:
                self.score = score - 9
            else:
                self.score = score

    def five_card_win(self):
        if len(self.cards) == 5 and self.score <= 21:
            return True
        else:
            return False

    def print_cards(self, showOnlyFirstCard=False):
        if len(self.cards) == 0:
            return

        card_str = []

        for card in self.cards:
            if card == 1:
                card_str.append("A")
            elif card == 11:
                card_str.append("J")
            elif card == 12:
                card_str.append("Q")
            elif card == 13:
                card_str.append("K")
            else:
                card_str.append(str(card))

        if showOnlyFirstCard:
            print(f"{self.name} cards -> [" + card_str[0] + "]")
        else:
            print(f"{self.name} cards -> {card_str}")
