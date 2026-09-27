'''https://projecteuler.net/problem=87'''
# The smallest number expressible as the sum of a prime square, prime cube, and
# prime fourth power is 28. In fact, there are exactly four numbers below fifty
# that can be expressed in such a way:

# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4

# How many numbers below fifty million can be expressed as the sum of a prime
# square, prime cube, and prime fourth power?

from math import isqrt
from resources.useful_functions import sieve_Eratosthenes


def sum_prime_powers(bound):
    '''Calculates hoy many numbers can be expressed as the sum of a prime
    square, prime cube and prime fourth power.'''
    # Find prime bound
    prime_bound = isqrt(bound - 24) + 1
    # Get all primes up to prime_bound
    primes = sieve_Eratosthenes(prime_bound)

    # Calculate all possible sums of prime powers
    prime_squares = [p**2 for p in primes]
    prime_cubes = [p**3 for p in primes]
    prime_fourths = [p**4 for p in primes]

    sums = set()
    # Run through all prime squares
    for s in prime_squares:
        if s >= bound:
            break
        # All prime cubes
        for c in prime_cubes:
            total = s + c
            if total >= bound:
                break
            # All prime fourths
            for f in prime_fourths:
                total = s + c + f
                # If at any point the total is greater than the bound, break
                if total >= bound:
                    break
                sums.add(total)
    return len(sums)


def main():
    '''Main code of module.'''
    print(sum_prime_powers(50))
    print(sum_prime_powers(50000000))  # 1097343, 0.26s


if __name__ == '__main__':
    main()
