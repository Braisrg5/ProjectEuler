'''https://projecteuler.net/problem=54'''
# In the card game poker, a hand consists of five cards and are ranked, from
# lowest to highest, in the following way:
#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the
# highest value winds; for example, a pair of eights beats a pair of fives (see
# example 1 below). But if two ranks tie, for example, both players have a pair
# of queens, then highest cards in each hand are compared (see example 4
# below); if the highest cards tie then the next highest cards are compared,
# and so on.

# Consider the following five hands dealt to two players:
#     Hand          Player 1              Player 2        Winner
#     Hand #1      5H 5C 6S 7S KD      2C 3S 8S 8D TD     Player 2
#                 Pair of Fives       Pair of Eights

#     Hand #2      5D 8C 9S JS AC      2C 5C 7D 8S QH     Player 1
#                 Highest card Ace    Highest card Queen

#     Hand #3      2D 9C AS AH AC      3D 6D 7D TD QD     Player 2
#                 Three Aces          Flush with Diamonds
#     Hand #4      4D 6S 9H QH QC      3D 6D 7H QD QS     Player 1
#                 Pair of Queens      Pair of Queens
#                 Highest card Nine   Highest card Seven

#     Hand #5      2H 2D 4C 4D 4S      3C 3D 3S 9S 9D     Player 1
#                 Full House          Full House
#                 with Three Fours   with Three Threes

# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space): the
# first five are Player 1's cards and the last five are Player 2's cards. You
# can assume that all hands are valid (no invalid characters or repeated
# cards), each player's hand is in no specific order, and in each hand there is
# a clear winner.

# How many hands does Player 1 win?
from collections import Counter


class Hand:
    '''Class representing the rank of a hand in poker.'''

    # Possible card values
    all_vals = [
            '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    # Custom order for the values
    order_vals = dict(zip(all_vals, range(len(all_vals))))
    # Possible ranks (including empty/unknown rank)
    all_ranks = ['', 'High Card', 'One Pair', 'Two Pairs', 'Three of a Kind',
                 'Straight', 'Flush', 'Full House', 'Four of a Kind',
                 'Straight Flush', 'Royal Flush']
    # Custom order for the ranks
    order_ranks = dict(zip(all_ranks, range(len(all_ranks))))

    def __init__(self, cards_string):
        self.cards = cards_string.split()
        self.vals, self.num_vals, self.suits = self.set_vals_and_suits()

    def set_vals_and_suits(self):
        '''Sets the values, the numeric values and the suits of the cards.'''
        vals = [card[0] for card in self.cards]
        # Ordered values of the cards with custom sort
        vals.sort(key=lambda val: self.order_vals[val])
        # Numeric values of the cards with custom sort
        num_vals = [self.order_vals[val] for val in vals]
        suits = [card[1] for card in self.cards]
        return vals, num_vals, suits

    def flush_and_straight(self):
        '''Helper function to self.calculate_rank.
        Checks all possible combinations of flush and straight.'''
        rank, max_val, rest_vals = '', -1, []
        # Generate new list with range lowest and highest numeric values
        min_max = list(range(self.num_vals[0], self.num_vals[4] + 1))
        # If the list hasn't changed, cards are consecutive
        consecutive = self.num_vals == min_max
        # And we also need to consider the case of a wheel straight (1*)
        # where the card values are 2, 3, 4, 5 and Ace
        wheel_num_vals = [0, 1, 2, 3, 12]
        wheel = self.num_vals == wheel_num_vals
        # Straight if the cards are consecutive or wheel
        if consecutive or wheel:
            rank = 'Straight'

        # If all cards from the same suit
        if len(set(self.suits)) == 1:
            if rank == 'Straight':
                # Royal Flush if smallest card is a 10
                if self.num_vals[0] == 8:
                    rank = 'Royal Flush'
                else:
                    rank = 'Straight Flush'
            # Flush if not Straight
            else:
                rank = 'Flush'
                # Add cards different than max to compare between flushes
                rest_vals += self.num_vals[:-1]

        # If any value has been specified for rank
        if rank:
            if wheel:
                # Value for the wheel
                max_val = 3
            else:
                # Value for anything else (biggest card value)
                max_val = self.num_vals[-1]

        # Value for the current rank
        rank_val = self.order_ranks[rank]
        return (rank, rank_val, max_val, rest_vals)

    def rank_repeated_cards(self, rank, rank_val, max_val, rest_vals):
        '''Helper function to self.calculate_rank.
        Looks for repeated cards and assigns the appropriate rank.'''
        count_num_vals = Counter(self.num_vals)
        # Returns a list [(value, count),(value, count),...] ordered by
        # count and then by value (because num_vals is already sorted)
        popular = count_num_vals.most_common()
        most_popular = popular[0]

        # Only combinations for len == 2 are 4-1 and 3-2 (5-0 in Balatro)
        if len(popular) == 2:
            # Four of a Kind if the most common count is equal to four
            if most_popular[1] == 4:
                rank = 'Four of a Kind'
                rest_vals += [popular[1][0]]
            # Full House if it is equal to three
            else:
                rank = 'Full House'
                rest_vals += [popular[1][0]]*2
            max_val = most_popular[0]
            rank_val = self.order_ranks[rank]

        # Only if the rank is less than Straight
        if rank_val <= 4:
            # Three of a Kind if most common is equal to three
            if most_popular[1] == 3:
                rank = 'Three of a Kind'
                max_val = most_popular[0]
                rest_vals += [popular[1][0]] + [popular[2][0]]
            # Two Pairs if first and second most common are equal to two
            elif popular[0][1] == 2 and popular[1][1] == 2:
                rank = 'Two Pairs'
                max_val = popular[1][0]
                # Add card not in pairs and lowest valued pair (that order)
                rest_vals += [popular[2][0]]+[popular[0][0]]*2
            # One Pair if previous test failed and most common is two
            elif popular[0][1] == 2:
                rank = 'One Pair'
                max_val = popular[0][0]
                # Add the remaining cards
                rest_vals += [popular[1][0]] \
                    + [popular[2][0]] + [popular[3][0]]
            # High Card if all tests until now have failed
            else:
                rank = 'High Card'
                max_val = self.num_vals[-1]
                # Add the remaining cards
                rest_vals += self.num_vals[:-1]
            rank_val = self.order_ranks[rank]
        return (rank, rank_val, max_val, rest_vals)

    def calculate_rank(self):
        '''Calculates and returns the rank of the hand.'''
        # Ranks and values obtained from flush and straight
        (rank, rank_val, max_val, rest_vals) = self.flush_and_straight()

        # Not Royal Flush or Straight Flush
        if rank_val <= 8:
            # Ranks and values obtained from checking repeating cards
            (rank, rank_val, max_val, rest_vals
             ) = self.rank_repeated_cards(rank, rank_val, max_val, rest_vals)
        return (rank, rank_val, max_val, rest_vals)


def load_hands(path):
    '''Loads the hands from a file and returns them as a list of tuples.'''
    with open(path, 'r', encoding='utf-8') as file:
        hands = [[hands[:14], hands[15:29]] for hands in file]
    return [(hand[0], hand[1]) for hand in hands]


def which_hand_wins(hand_pair):
    '''Returns 1 if the first hand wins, 2 if the second hand wins.'''
    hand1, hand2 = hand_pair
    hand1_rank = Hand(hand1).calculate_rank()
    hand2_rank = Hand(hand2).calculate_rank()
    winner = None

    # Ranks are equal
    if hand1_rank[1] == hand2_rank[1]:
        # Max cards are also equal
        if hand1_rank[2] == hand2_rank[2]:
            # We compare the rest of the cards from biggest to smallest
            for i in range(len(hand1_rank[3])-1, -1, -1):
                # If a card from hand1 is higher than a card from hand2,
                # hand1 wins, otherwise hand2 wins
                if hand1_rank[3][i] > hand2_rank[3][i]:
                    winner = 1
                    break
                if hand1_rank[3][i] < hand2_rank[3][i]:
                    winner = 2
                    break
            # Extreme case of a tie, no winner
            if not winner:
                print('There has been a tie!!!')
                return winner

        # Same rank but max cards are different
        elif hand1_rank[2] > hand2_rank[2]:
            winner = 1
        else:
            winner = 2

    # Different rank
    elif hand1_rank[1] > hand2_rank[1]:
        winner = 1
    else:
        winner = 2
    return winner


def wins_first_player(path):
    '''Calculates number of times the first player wins in the pairs of hands
    found in the file in the given path.'''
    hand_pairs = load_hands(path)
    wins = sum(which_hand_wins(hand_pair) == 1 for hand_pair in hand_pairs)
    return wins


if __name__ == '__main__':
    print(wins_first_player('resources/0054_poker.txt'))  # 376, 0.011s


# ----- #
# Notes #
# ----- #

# (1*)
# If there is a wheel straight, self.vals are ['2', '3', '4', '5', 'A'] and
# self.num_vals are [0, 1, 2, 3, 4, 12]
