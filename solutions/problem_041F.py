'''https://projecteuler.net/problem=41'''
# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
# and is also prime.

# What is the largest n-digit pandigital prime that exists?
from itertools import permutations
from resources.useful_functions import is_prime


def generate_pandigitals(n):
    '''Generates all n-digit pandigital numbers from biggest to smallest.'''
    pandigitals = list(permutations([str(i) for i in range(1, n+1)]))
    return sorted(int(''.join(p)) for p in pandigitals)[::-1]


def largest_pandigital_prime():
    '''Returns the largest 9-digit pandigital prime that exists.'''
    # n can't be 9, 8, 6, 5, 3 or 2 because of (1*).
    for n in range(7, 0, -3):
        # Generate all n-digit pandigital numbers from biggest to smallest.
        pandigital = generate_pandigitals(n)
        for num in pandigital:
            if is_prime(num):
                return num
        print('No primes found for n = ', n)
    # If no prime is found for any n, return -1.
    return -1


if __name__ == '__main__':
    print(largest_pandigital_prime())  # 7652413, 0.002s


# ----- #
# Notes #
# ----- #

# (1*)
# For n = 9, 1+2+3+4+5+6+7+8+9 = 45, which is divisible by 3, so not prime.
# For n = 8, 1+2+3+4+5+6+7+8 = 36, which is divisible by 3, so not prime.
# For n = 7, 1+2+3+4+5+6+7 = 28, which is not divisible by 3, so may be prime.

# Same goes for n = 6, sum = 21, and n = 5, sum = 15, which are divisible by 3.
# And n = 3, sum = 6, and n = 2, sum = 3.
