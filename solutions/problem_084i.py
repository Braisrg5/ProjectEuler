'''https://projecteuler.net/problem=84'''
import random
from tqdm import tqdm


class Player:
    '''Class representing the Monopoly board.'''

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
    print(modal_string)  # 102400, 1.02s

    odds = montecarlo_monopoly(4, 1000000)
    modal_string = ''.join(f'{k:02}' for k in list(odds.keys())[:3])
    print(modal_string)  # 101524, 1.02s


if __name__ == '__main__':
    main()
