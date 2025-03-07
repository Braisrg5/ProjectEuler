'''https://projecteuler.net/problem=35'''
# The number, 197, is called a circular prime because all rotations of
# the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
# 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?
from resources.useful_functions import (
    sieve_Eratosthenes, digits_odd
)


def rotate_number(n):
    '''Returns all rotations of the digits of a number n.'''
    n = str(n)
    rotations = {int(n[i:] + n[:i]) for i in range(len(n))}
    return rotations


def circular_primes_v4(bound):
    '''Finds how many circular primes are there below one million.'''
    # Generate primes using the sieve up to bound
    primes = sieve_Eratosthenes(bound)[5:]
    primes_set = set(primes)  # Convert to set for O(1) lookups

    # Initialize the set of circular primes with one digit primes and 11
    circ_primes = set([2, 3, 5, 7, 11])
    for prime in primes:
        # Only consider odd digits for circular primes, because if any digit is
        # even, at least one rotation will not be prime.
        if digits_odd(prime):
            # Find every distinct rotation of the prime number
            rotations = rotate_number(prime)
            # If all rotations are prime, p is circular
            if all(p in primes_set for p in list(rotations)):
                # | is the operator for set union
                circ_primes = circ_primes | rotations

    return len(circ_primes)


if __name__ == '__main__':
    print(rotate_number(197))  # [197, 971, 719]
    print(circular_primes_v4(100))  # 13
    print(circular_primes_v4(1000000))  # 55, 0.13s
