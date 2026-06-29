'''Test module'''
from time import perf_counter
from math import floor, sqrt
from collections import Counter

from useful_functions import (
    digit_sum, prime_factors
    )

# Avoid error messages
start = perf_counter()
start += 1


def sieve_v1(n):
    '''Returns a list of prime numbers up to n using the Sieve of Eratosthenes.
    '''
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, floor(sqrt(n))+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i]]


def sieve_v2(n):
    '''Returns a list of prime numbers up to n using the Sieve of Eratosthenes.
    '''
    nums = list(range(3, n + 1, 2))
    nums_dict = {num: True for num in nums}
    for num in nums_dict:
        if num * num > n:
            break
        if nums_dict[num]:
            for k in range(num, floor(n / num) + 1, 2):
                nums_dict[num * k] = False
    return [2] + [k for k, v in nums_dict.items() if v]

# start = perf_counter()
# sieve_v1(1000000000)
# print(perf_counter() - start)


def transform_factors(n):
    '''Transforms the list of factors of a number into a list of the powers of
    the factors.'''
    pf = prime_factors(n)
    fact_count = Counter(pf)
    return [fact ** count for fact, count in fact_count.items()]


# for i in range(20, 100000000):
#     factors = transform_factors(i)
#     if len(factors) - len(set(factors)) != 0:
#         print("HEY")

def is_pentagonal(p):
    '''Checks if a number is pentagonal.'''
    # Formulas are derived in (3*)
    n = (1 + sqrt(1 + 24*p))/6
    return n.is_integer()


def is_pentagonal_v2(p):
    '''Checks if a number is pentagonal.'''
    return sqrt(1 + 24*p) % 6 == 5


def is_hexagonal(h):
    '''Checks if a number is hexagonal.'''
    # Formulas are derived in (3*)
    n = (1 + sqrt(1 + 8*h))/4
    return n.is_integer()


def is_hexagonal_v2(h):
    '''Checks if a number is hexagonal.'''
    return sqrt(1 + 8*h) % 4 == 3


# MAX = 1000000
# start = perf_counter()
# for i in range(1, MAX):
#     prime_factors(i)
# print(perf_counter() - start)

# start = perf_counter()
# for i in range(1, MAX):
#     prime_factors_sieve(i)
# print(perf_counter() - start)

# start = perf_counter()
# primes1 = sieve_Eratosthenes(MAX)
# print(perf_counter()-start)

# start = perf_counter()
# primes2 = sieve_Pritchards_wheel(MAX)
# print(perf_counter()-start)

# print(primes2)

MAX = 100**100

for a in range(1, 100):
    for b in range(1, 100):
        sum1 = digit_sum(MAX)
