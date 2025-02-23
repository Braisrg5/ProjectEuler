'''https://projecteuler.net/problem=26
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:
                1/2 = 0.5
                1/3 = 0.(3)
                1/4 = 0.25
                1/5 = 0.2
                1/6 = 0.1(6)
                1/7 = 0.(142857)
                1/8 = 0.125
                1/9 = 0.(1)
                1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
'''
from resources.useful_functions import sieve_Eratosthenes


def recurring_cycle(d):
    '''Finds the length of the repitend of 1/d by making a list of the
    remainders of the division of 10**i by d, where i goes from 0 to d-1. When
    a remainder is repeated, the length of the repitend is the number of
    remainders between the current one and the repeated one.'''
    remainders = [1]
    D = 10
    for i in range(d):
        r = D % d
        # Exact division
        if r == 0:
            return 0
        # Every remainder is added if it is not repeated
        elif r not in remainders:
            remainders.append(r)
        # If the remainder is repeated, we've found the beginning and end of
        # the repitend, so we can find the length
        else:
            start = remainders.index(r)
            return len(remainders[start:])
        # Base 10 division
        D = r * 10
    # Something went very wrong if this is executed
    return -1


def longest_recurring_cycle(bound):
    '''Finds the largest repitend of 1/d where d < bound.'''
    primes = sieve_Eratosthenes(bound)
    d_cycle = dict()
    for d in primes:
        d_cycle[d] = recurring_cycle(d)
    return max(d_cycle, key=d_cycle.get)


if __name__ == '__main__':
    print(longest_recurring_cycle(11))  # 7
    print(longest_recurring_cycle(1000))  # 983, 0.12s
