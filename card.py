import random
from random import shuffle

#card_tuple = (face,suit,value)

CARD_SUITS = ["Diamonds",
              "Clubs",
              "Hearts",
              "Spades"]

CARD_VALUES = list(range(1,11)) + [10, 10, 10]

CARD_FACES = ["A"] + list(range(2,11)) + "J Q K".split()

class Card(object):

    def __init__(self):
        self.value = random.choice(CARD_VALUES)

class Deck(Card):

    def create_deck(self):
        deck_of_cards = []
        index = 0
        for value in CARD_VALUES:
            for suit in CARD_SUITS:
                temp_tup = (CARD_FACES[index], suit, value)
                deck_of_cards.append(temp_tup)
            index += 1
        return deck_of_cards

    def next_card(self):
        try:
            return self.deck.pop(0)
        except IndexError:
            return None

    def __init__(self):
        self.deck = self.create_deck()
        shuffle(self.deck)
