import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        # delegates the [] operator to self._cards
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(choice(deck))

print(len(deck))
print(deck[0])
print(deck[-1])

# By implementing the __getitem__ special method, the deck is also iterable:
for card in deck:
    print(card)

# The deck can also be iterated in reverse:
for cards in reversed(deck):
    print(card)

# A common system of ranking cards is by rank (with aces being highest), then by suit in the order of spades then hearts, diamonds and clubs(lowest). Here is a function that ranks cards by that rule, returning 0 for the 2 of clubs and 51 for the ace of spades:

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# Given spades_high, we can now list our deck in order of increasing rank:
for card in sorted(deck, key=spades_high):
    print(card)
