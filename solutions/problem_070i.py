'''https://projecteuler.net/problem=70'''
# Euler's totient function, phi(n) [sometimes called the phi function], is
# defined as the number of positive integers not exceeding n which are
# relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less
# than or equal to nine and relatively prime to nine, phi(9) = 6.
# The number 1 is considered to be relatively prime to every positive number,
# so phi(1) = 1.

# Interestingly, phi(87109) = 79180, and it can be seen that 87109 is a
# permutation of 79180.

# Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and
# ratio n/phi(n) produces a minimum.
from time import perf_counter
from math import isqrt
from resources.useful_functions import sieve_Eratosthenes, sieve_totient


def permuted_min_ratio(bound):
    '''Finds the value of n < bound for which phi(n) is a permutation of n and
    the ratio n/phi(n) produces a minimum.'''
    min_ratio = float('inf')
    obj_n = -1

    start = perf_counter()
    phi = sieve_totient(bound)
    print(f"Totient function calculated in {perf_counter()-start} seconds")

    for n, val in enumerate(phi):
        if n in (0, 1):
            continue
        ratio = n/val
        if ratio < min_ratio and sorted(str(n)) == sorted(str(val)):
            min_ratio = ratio
            obj_n = n
    return obj_n


def permuted_min_ratio_v2(bound):
    '''Finds the value of n < bound for which phi(n) is a permutation of n and
    the ratio n/phi(n) produces a minimum.
    Explained in (2*).'''
    min_ratio = float('inf')
    obj_n = -1
    primes_bound = isqrt(bound)*10
    primes = sieve_Eratosthenes(primes_bound)[::-1]
    len_primes = len(primes)
    for i in range(len_primes):
        pi = primes[i]
        for j in range(i+1, len_primes):
            pj = primes[j]
            n = pi*pj
            if n > bound:
                continue
            phi = (pi-1)*(pj-1)
            ratio = n/phi
            if ratio < min_ratio and sorted(str(n)) == sorted(str(phi)):
                min_ratio = ratio
                obj_n = n
    return obj_n, min_ratio


if __name__ == '__main__':
    # init = perf_counter()
    # print(permuted_min_ratio(10000000))  # 8319823, 6.67s
    # print(f"Calculation completed in {perf_counter()-init} seconds")
    init = perf_counter()
    print(permuted_min_ratio_v2(10000000))  # 8319823, 0.48s
    print(f"Calculation completed in {perf_counter()-init} seconds")
