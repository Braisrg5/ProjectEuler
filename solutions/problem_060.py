'''https://projecteuler.net/problem=60
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the smallest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
'''
from resources.useful_functions import sieve_Eratosthenes, is_prime
from itertools import combinations_with_replacement as combinations_wr
from math import log10, floor
from sympy import isprime
from time import perf_counter


def concats(nums):
    '''Returns a list of all concatenations of the numbers in nums.'''
    concatenations = set()
    len_nums = len(nums)
    for i in range(len_nums-1):
        n1 = nums[i]
        digits_n1 = floor(log10(n1)) + 1
        for j in range(i+1, len_nums):
            n2 = nums[j]
            digits_n2 = floor(log10(n2)) + 1
            concatenations.add(n1*10**(digits_n2) + n2)
            concatenations.add(n2*10**(digits_n1) + n1)
    return concatenations


def prime_pair_sets(n, bound):
    '''Finds the smallest sum for a set of n primes for which any two primes
    concatenate to produce another prime.'''
    primes_small = sieve_Eratosthenes(bound)[1:]
    primes_big = sieve_Eratosthenes(bound**2)[1:]
    primes_s = set(primes_big)
    print("Primes_big has been generated")
    prime_combinations = combinations_wr(primes_small, n)
    start = perf_counter()
    for combination in prime_combinations:
        if all(p in primes_s for p in concats(combination)):
            return sum(combination)
        if perf_counter() - start > 5:
            print(combination)
            start = perf_counter()
    # bound not large enough
    return -1


def new_concats(old, new):
    '''Returns a list of all concatenations of the new number with each number
    in old.'''
    concatenations = set()
    for p in old:
        concatenations = concatenations.union(concats([p, new]))
    return concatenations


def prime_pair_sets_v2(n, bound):
    '''Finds the smallest sum for a set of n primes for which any two primes
    concatenate to produce another prime.'''
    primes_big = sieve_Eratosthenes(bound**2)[1:]
    primes_small = [p for p in primes_big if p < bound]
    num_primes = len(primes_small)
    primes_s = set(primes_big)
    print("Generated all the primes.")
    for i in range(num_primes):
        p1 = primes_small[i]
        for j in range(i+1, num_primes):
            p2 = primes_small[j]
            if all(p in primes_s for p in new_concats([p1], p2)):
                for k in range(j+1, num_primes):
                    p3 = primes_small[k]
                    if all(p in primes_s for p in new_concats([p1, p2], p3)):
                        for m in range(k+1, num_primes):
                            p4 = primes_small[m]
                            if all(p in primes_s
                                   for p in new_concats([p1, p2, p3], p4)):
                                for n in range(m+1, num_primes):
                                    p5 = primes_small[n]
                                    if all(p in primes_s
                                           for p in new_concats([
                                               p1, p2, p3, p4], p5)):
                                        return p1 + p2 + p3 + p4 + p5
    # bound not large enough
    return -1


def prime_pair_sets_v3(n, bound):
    '''Finds the smallest sum for a set of n primes for which any two primes
    concatenate to produce another prime.'''
    def recursive_helper(n, index, old):
        if n == 0:
            return old
        for i in range(index + 1, num_primes):
            p = primes_small[i]
            if all(p in primes_set for p in new_concats(old, p)):
                sol = recursive_helper(n - 1, i, old + [p])
                if sol is not None:
                    return sol

    primes_big = sieve_Eratosthenes(bound**2)[1:]
    primes_set = set(primes_big)
    primes_small = [p for p in primes_big if p < bound]
    num_primes = len(primes_small)
    print("Generated all the primes.")
    for i in range(num_primes):
        p1 = primes_small[i]
        for j in range(i+1, num_primes):
            p2 = primes_small[j]
            if all(p in primes_set for p in new_concats([p1], p2)):
                sol = recursive_helper(n - 2, j, [p1, p2])
                if sol is not None:
                    return sol


def prime_pair_sets_v4(n, bound):
    '''Finds the smallest sum for a set of n primes for which any two primes
    concatenate to produce another prime.'''
    def recursive_helper(n, index, old):
        if n == 0:
            return old
        for i in range(index + 1, num_primes):
            p = primes_small[i]
            if all(is_prime(p) for p in new_concats(old, p)):
                sol = recursive_helper(n - 1, i, old + [p])
                if sol is not None:
                    return sol

    primes_small = sieve_Eratosthenes(bound)[1:]
    num_primes = len(primes_small)
    print("Generated all the primes.")
    for i in range(num_primes):
        p1 = primes_small[i]
        for j in range(i+1, num_primes):
            p2 = primes_small[j]
            if all(is_prime(p) for p in new_concats([p1], p2)):
                sol = recursive_helper(n - 2, j, [p1, p2])
                if sol is not None:
                    return sol


def prime_pair_sets_v5(n, bound):
    '''Finds the smallest sum for a set of n primes for which any two primes
    concatenate to produce another prime.'''
    def recursive_helper(n, index, old):
        if n == 0:
            return old
        for i in range(index + 1, num_primes):
            p = primes_small[i]
            if all(isprime(p) for p in new_concats(old, p)):
                sol = recursive_helper(n - 1, i, old + [p])
                if sol is not None:
                    return sol

    primes_small = sieve_Eratosthenes(bound)[1:]
    num_primes = len(primes_small)
    print("Generated all the primes.")
    for i in range(num_primes):
        p1 = primes_small[i]
        for j in range(i+1, num_primes):
            p2 = primes_small[j]
            if all(isprime(p) for p in new_concats([p1], p2)):
                sol = recursive_helper(n - 2, j, [p1, p2])
                if sol is not None:
                    return sol


if __name__ == '__main__':
    # Generate all primes beforehand
    # print(prime_pair_sets_v3(5, 10000))  # 26033, 6.17s
    # Is_prime function in resources.useful_functions
    # print(prime_pair_sets_v4(5, 10000))  # 26033, 6.91s
    # Sympy's isprime function
    print(prime_pair_sets_v5(5, 10000))  # 26033, 2.40s
