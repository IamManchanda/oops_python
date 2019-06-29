""" Python classes """

from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"This is a Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        min_count_num = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        else:
            print(f"Going to remove {min_count_num} cards")
        cards = self.cards[-min_count_num:]
        self.cards = self.cards[:-min_count_num]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if (self.count() < 52):
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

d = Deck()

for c in d:
    print(c)
    
print(f"{d}\n")
d.shuffle()
print(f"Shuffled Cards: {d.cards}\n")

card = d.deal_card()
print(f"Removed Card: {card}\n")

hand = d.deal_hand(5)
print(f"Removed Cards: {hand}\n")

print(f"Left Cards: {d.cards}")
