'''https://projecteuler.net/problem=54
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:
    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value winds; for example, a pair of eights beats a pair of fives (see example
1 below). But if two ranks tie, for example, both players have a pair of
queens, then highest cards in each hand are compared (see example 4 below); if
the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
    Hand          Player 1              Player 2        Winner
    Hand #1      5H 5C 6S 7S KD      2C 3S 8S 8D TD     Player 2
                Pair of Fives       Pair of Eights

    Hand #2      5D 8C 9S JS AC      2C 5C 7D 8S QH     Player 1
                Highest card Ace    Highest card Queen

    Hand #3      2D 9C AS AH AC      3D 6D 7D TD QD     Player 2
                Three Aces          Flush with Diamonds
    Hand #4      4D 6S 9H QH QC      3D 6D 7H QD QS     Player 1
                Pair of Queens      Pair of Queens
                Highest card Nine   Highest card Seven

    Hand #5      2H 2D 4C 4D 4S      3C 3D 3S 9S 9D     Player 1
                Full House          Full House
                with Three Fours   with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
'''
from collections import Counter


class Hand:
    '''Class representing the rank of a hand in poker.'''

    def __init__(self, cards):
        self.cards = cards.split(' ')
        self.vals_and_suits()
        self.max_val = -1  # Should change eventually
        self.rest = []  # Excess cards not in particular hand
        self.calculate_rank()

    def vals_and_suits(self):
        # Custom sort order
        self.order = [
            '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'
            ]
        self.order_dict = dict(zip(self.order, range(len(self.order))))
        self.vals = [card[0] for card in self.cards]
        # Ordered numbers of the cards with custom sort
        self.vals.sort(key=lambda val: self.order_dict[val])
        # Numeric values of the cards with custom sort
        self.num_vals = [self.order_dict[val] for val in self.vals]
        # Suits of the cards
        self.suits = [card[1] for card in self.cards]

    def flush_and_straight(self):
        '''Checks all combinations of flush and straight.'''
        # Flush if all cards from the same suit
        self.flush = (len(set(self.suits)) == 1)
        # self.max_val = self.num_vals[-1]

        # Straight if the cards are consecutive or wheel
        # Generate new list with range lowest and highest numeric values
        min_max = list(range(self.num_vals[0], self.num_vals[4] + 1))
        # If the list hasn't changed, it is a straight
        normal_straight = self.num_vals == min_max
        # self.max_val = self.num_vals[-1]
        # And we also need to consider the case of a wheel straight (1*)
        wh_min_max = list(range(self.num_vals[0], self.num_vals[3] + 1))
        print(wh_min_max)
        two_to_five = (self.num_vals[:4] == wh_min_max and self.vals[0] == '2')
        wheel = (two_to_five and self.vals[-1] == 'A')
        # self.max_val = 3
        self.straight = (normal_straight or wheel)

        # Straight flush if straight and flush
        self.straight_flush = self.straight and self.flush

        # Royal flush if straight flush and smallest card is a 10
        self.Royal_flush = self.straight_flush and self.vals[0] == 'T'

    def repeated_cards(self):
        count_num_vals = Counter(self.num_vals)
        popular = count_num_vals.most_common()
        most_popular = popular[0]

        # Four of a kind if
        self.four_of_a_kind = (most_popular[1] == 4)
        self.max_val = most_popular[0]

    def calculate_rank(self):
        self.flush_and_straight()


def load_hands(path):
    '''Loads the hands from a file and returns them as a list of tuples.'''
    with open(path, 'r') as file:
        hands = [[hands[:14], hands[15:29]] for hands in file]
    return [(hand[0], hand[1]) for hand in hands]


if __name__ == '__main__':
    hand_pairs = load_hands('resources/0054_poker.txt')

    # test
    # hand1 = Hand('6C 7C 8C 9C TC')
    hand2 = Hand('AC 4C 3C 5C 2C')
    print(hand2.vals)
    # print(hand1.is_straight())
    print('Hand2 is a straight flush?', hand2.Royal_flush)


'''
#-------#
# Notes #
#-------#

(1*)
If there is a wheel straight, self.vals are ['2', '3', '4', '5', 'A'] and
self.num_vals are [0, 1, 2, 3, 4, 12]
'''
