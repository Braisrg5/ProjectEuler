"""The number, 197, is called a circular prime because all rotations of
the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""


from resources.useful_functions import (
    sieve_Eratosthenes, is_prime, digits_odd
)
from time import perf_counter


def rotate_number(n):
    """Returns all rotations of the digits of a number n."""
    n = str(n)
    rotations = {int(n[i:] + n[:i]) for i in range(len(n))}
    return list(rotations)


def circular_primes(bound):
    primes = sieve_Eratosthenes(bound)
    num_circular = 0
    start = perf_counter()
    for prime in primes:
        if prime < 10:
            num_circular += 1
        else:
            rotations = rotate_number(prime)
            if len(rotations) == 1:
                num_circular += 1
            elif all(p in primes for p in rotations):
                num_circular += len(rotations)
                for p in rotations[1:]:
                    primes.remove(p)
        if perf_counter() - start > 2:
            print(prime)
            start = perf_counter()
    return num_circular


def circular_primes_v2(bound):
    primes = sieve_Eratosthenes(bound)
    num_circular = 0
    for prime in primes:
        start = perf_counter()
        if prime < 10:
            num_circular += 1
        else:
            rotations = rotate_number(prime)
            if len(rotations) == 1:
                num_circular += 1
            elif all(is_prime(p) for p in rotations):
                num_circular += len(rotations)
                for p in rotations:
                    primes.remove(p)
        if perf_counter() - start > 2:
            print(prime)
            start = perf_counter()
    return num_circular


def circular_primes_v3(bound):
    primes = sieve_Eratosthenes(bound)
    circ_primes = set()
    for prime in primes:
        if prime < 10:
            circ_primes.add(prime)
        else:
            rotations = rotate_number(prime)
            if len(rotations) == 1:
                circ_primes.add(prime)
            elif all(is_prime(p) for p in rotations):
                circ_primes = circ_primes | set(rotations)
    return len(circ_primes)


def circular_primes_v4(bound):
    primes = sieve_Eratosthenes(bound)
    circ_primes = set()
    for prime in primes:
        if prime < 10:
            circ_primes.add(prime)
        elif digits_odd(prime):
            rotations = rotate_number(prime)
            if len(rotations) == 1:
                circ_primes.add(prime)
            elif all(is_prime(p) for p in rotations):
                circ_primes = circ_primes | set(rotations)
    return len(circ_primes)


if __name__ == '__main__':
    print(rotate_number(197))  # [197, 971, 719]
    print(circular_primes(100))  # 13
    # print(circular_primes(1000000))  # 55, 172s
    # print(circular_primes_v2(1000000))  # 55, 1.40s
    # print(circular_primes_v3(1000000))  # 55, 1.23s
    print(circular_primes_v4(1000000))  # 55, 0.43s
