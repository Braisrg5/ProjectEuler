'''https://projecteuler.net/problem=46'''
# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
#                 9=7+2*12
#                 15=7+2*22
#                 21=3+2*32
#                 25=7+2*32
#                 27=19+2*22
#                 33=31+2*12
# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?
from math import isqrt


def sieve_eratosthenes_mod(bound):
    '''Returns a list of primes up to bound. It also returns a list of
    composite odds for this particular problem.'''
    sieve = [True] * (bound+1)
    sieve[0] = sieve[1] = False
    odds = []
    for i in range(2, isqrt(bound)+1):
        if sieve[i]:
            for j in range(i*i, bound+1, i):
                sieve[j] = False
        # Odds remain in the list after multiples of 2 are excluded
        if i == 2:
            odds = [i for i in range(3, bound+1) if sieve[i]]

    primes = [i for i in range(2, bound+1) if sieve[i]]
    # Composite odds are the difference between odds and primes
    composite = list(set(odds)-set(primes))
    return primes, composite


def prime_twice_square(bound, primes):
    '''Returns a list of numbers that can be written as the sum of a prime and
    twice a square.'''
    combinations = []
    for i in primes:
        # This limit for j is found in (1*)
        maxj = isqrt((bound-i)//2) + 1
        for j in range(1, maxj):
            combinations.append(i+2*j**2)
    return combinations


def missing_odd_composite(bound):
    '''Finds all the odd composite lower than bound that cannot be written as
    the sum of a prime and twice a square.'''
    primes, composite = sieve_eratosthenes_mod(bound)
    # We exclude the first prime (2) because of the problem statement,
    # 2 plus twice a square would not be odd.
    ptwicesq = prime_twice_square(bound, primes[1:])
    return set(composite)-set(ptwicesq)


if __name__ == '__main__':
    print(missing_odd_composite(6000))  # 5777, 0.004s


# ----- #
# Notes #
# ----- #

# (1*)
# We have a bound N for the primes and the composite numbers, so it wouldn't
# make sense to compute numbers ptwicesq that are greater than N, because when
# we subtract the ptwicesq from the composite numbers, it would be redundant to
# have numbers greater than N in the list. So, for each prime p, we want:
#             p+2*j^2 < N -> j^2 < (N-p)/2 -> j =< isqrt((N-p)/2).
