'''https://projecteuler.net/problem=84'''
# In the game, Monopoly, the standard board is set up in the following way:

#                 GO   A1  CC1  A2  T1  R1  B1  CH1  B2   B3  JAIL
#                 H2                                          C1
#                 T2                                          U1
#                 H1                                          C2
#                 CH3                                         C3
#                 R4                                          R2
#                 G3                                          D1
#                 CC3                                         CC2
#                 G2                                          D2
#                 G1                                          D3
#                 G2J  F3  U2   F2  F1  R3  E3  E2   CH2  E1  FP

# A player starts on the GO square and adds the scores on two 6-sided dice
# to determine the number of squares they advance in a clockwise direction.
# Without any further rules we would expect to visit each square with equal
# probability: 2.5%. However, landing on G2J (Go To Jail), CC (community
# chest), and CH (chance) changes this distribution.

# In addition to G2J, and one card from each of CC and CH, that orders the
# player to go directly to jail, if a player rolls three consecutive
# doubles, they do not advance the result of their 3rd roll. Instead they
# proceed directly to jail.

# At the beginning of the game, the CC and CH cards are shuffled. When a
# player lands on CC or CH they take a card from the top of the respective
# pile and, after following the instructions, it is returned to the bottom
# of the pile. There are sixteen cards in each pile, but for the purpose of
# this problem we are only concerned with cards that order a movement; any
# instruction not concerned with movement will be ignored and the player
# will remain on the CC/CH square.

#     • Community Chest (2/16 cards):

#      1. Advance to GO
#      2. Go to JAIL

#     • Chance (10/16 cards):

#      1. Advance to GO
#      2. Go to JAIL
#      3. Go to C1
#      4. Go to E3
#      5. Go to H2
#      6. Go to R1
#      7. Go to next R (railway company)
#      8. Go to next R
#      9. Go to next U (utility company)
#     10. Go back 3 squares.

# The heart of this problem concerns the likelihood of visiting a particular
# square. That is, the probability of finishing at that square after a roll.
# For this reason it should be clear that, with the exception of G2J for
# which the probability of finishing on it is zero, the CH squares will have
# the lowest probabilities, as 5/8 request a movement to another square, and
# it is the final square that the player finishes at on each roll that we
# are interested in. We shall make no distinction between "Just Visiting"
# and being sent to JAIL, and we shall also ignore the rule about requiring
# a double to "get out of jail", assuming that they pay to get out on their
# next turn.

# By starting at GO and numbering the squares sequentially from 00 to 39 we
# can concatenate these two-digit numbers to produce strings that correspond
# with sets of squares.

# Statistically it can be shown that the three most popular squares, in
# order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO
# (3.09%) = Square 00. So these three most popular squares can be listed
# with the six-digit modal string: 102400.

# If, instead of using two 6-sided dice, two 4-sided dice are used, find the
# six-digit modal string.
import random
from tqdm import tqdm


class Player:
    '''Class representing a Monopoly player.'''

    # List of the Monopoly squares
    board = [
        'GO',
        'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
        'JAIL',
        'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
        'FP',
        'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
        'G2J',
        'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2'
    ]

    # Board order
    board_order = dict(zip(range(len(board)), board))

    # List of the Chance cards
    ch_cards = [
        'Advance to GO', 'Go to JAIL', 'Go to C1', 'Go to E3', 'Go to H2',
        'Go to R1', 'Go to next R', 'Go to next R', 'Go to next U',
        'Go back 3 squares'
        ] + ['Skip']*6

    # List of the Community Chest cards
    cc_cards = ['Advance to GO', 'Go to JAIL'] + ['Skip']*14

    # Initiate player
    def __init__(self, dice=6):
        self.position = 0
        self.square = self.board[self.position]
        self.doubles = 0
        self.n = dice

    def throw(self):
        '''Throw the dice.'''
        # Throw 2 n-sided die
        die1 = random.randint(1, self.n)
        die2 = random.randint(1, self.n)
        if die1 == die2:
            self.doubles += 1
        else:
            self.doubles = 0
        return die1 + die2

    def community_chest(self):
        '''Draw a Community Chest card.'''
        # Draw a Community Chest card
        card = random.choice(self.cc_cards)

        if card == 'Advance to GO':
            self.position = 0
            self.square = self.board[self.position]
        elif card == 'Go to JAIL':
            self.position = 10
            self.square = self.board[self.position]

    def chance(self):
        '''Draw a Chance card.'''
        # Draw a Chance card
        card = random.choice(self.ch_cards)

        if card == 'Advance to GO':
            self.position = 0
        elif card == 'Go to JAIL':
            self.position = 10
        elif card == 'Go to C1':
            self.position = 11
        elif card == 'Go to E3':
            self.position = 24
        elif card == 'Go to H2':
            self.position = 39
        elif card == 'Go to R1':
            self.position = 5
        elif card == 'Go to next R':
            # Player is in CH1
            if self.position == 7:
                self.position = 15
            # Player is in CH2
            elif self.position == 22:
                self.position = 25
            # Player is in CH3
            else:
                self.position = 5
        elif card == 'Go to next U':
            # Player is in CH1 or CH3
            if self.position in (7, 36):
                self.position = 12
            # Player is in CH2
            else:
                self.position = 28
        elif card == 'Go back 3 squares':
            self.position -= 3
            self.position %= len(self.board)

        self.square = self.board[self.position]

    def move(self):
        '''Move the player on the board.'''
        # Move the player on the board
        result = self.throw()
        if self.doubles == 3:
            self.doubles = 0
            self.position = 10
            self.square = self.board[self.position]
            return

        # Landed on square
        self.position += result
        self.position %= len(self.board)
        self.square = self.board[self.position]

        # Check special cases
        if self.square == 'G2J':
            self.position = 10
            self.square = self.board[self.position]
        elif self.square in ('CC1', 'CC2', 'CC3'):
            self.community_chest()
        elif self.square in ('CH1', 'CH2', 'CH3'):
            self.chance()


def montecarlo_monopoly(dice, n=1000):
    '''Simulates a game of Monopoly and returns the most landed on squares.'''
    # Create a player
    player = Player(dice)
    # Create a list to store the number of times each square is landed on
    landed_on = [0]*40

    # Simulate player movement
    for _ in tqdm(range(n)):
        # Move the player
        player.move()
        # Increment the square landed on
        landed_on[player.position] += 1
    total = sum(landed_on)
    perc_landed = [el/total for el in landed_on]

    return dict(zip(
        [landed_on.index(el) for el in sorted(landed_on)[::-1][:20]],
        sorted(perc_landed)[::-1][:20]
        ))


def main():
    '''Main code of module.'''
    odds = montecarlo_monopoly(6, 1000000)
    modal_string = ''.join(f'{k:02}' for k in list(odds.keys())[:3])
    print(modal_string)  # 102400, 1.02s, results may differ due to chance

    odds = montecarlo_monopoly(4, 1000000)
    modal_string = ''.join(f'{k:02}' for k in list(odds.keys())[:3])
    print(modal_string)  # 101524, 1.02s, results may differ due to chance


if __name__ == '__main__':
    main()
