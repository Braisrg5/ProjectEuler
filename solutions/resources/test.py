from time import perf_counter
from math import floor, sqrt
from useful_functions import (
    prime_factors, sieve_Pritchards_wheel
    )
from collections import Counter

# Avoid error messages
start = perf_counter()
start += 1


def sieve_v1(N):
    '''Returns a list of prime numbers up to N using the Sieve of Eratosthenes.
    '''
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    for i in range(2, floor(sqrt(N))+1):
        if sieve[i]:
            for j in range(i*i, N+1, i):
                sieve[j] = False
    return [i for i in range(2, N+1) if sieve[i]]


def sieve_v2(N):
    nums = list(range(3, N + 1, 2))
    nums_dict = {num: True for num in nums}
    for num in nums_dict:
        if num * num > N:
            break
        if nums_dict[num]:
            for k in range(num, floor(N / num) + 1, 2):
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

def is_pentagonal(P):
    '''Checks if a number is pentagonal.'''
    # Formulas are derived in (3*)
    n = (1 + sqrt(1 + 24*P))/6
    return n.is_integer()


def is_pentagonal_v2(P):
    return sqrt(1 + 24*P) % 6 == 5


def is_hexagonal(H):
    '''Checks if a number is hexagonal.'''
    # Formulas are derived in (3*)
    n = (1 + sqrt(1 + 8*H))/4
    return n.is_integer()


def is_hexagonal_v2(H):
    return sqrt(1 + 8*H) % 4 == 3


'''MAX = 1000000
start = perf_counter()
for i in range(1, MAX):
    prime_factors(i)
print(perf_counter() - start)

start = perf_counter()
for i in range(1, MAX):
    prime_factors_sieve(i)
print(perf_counter() - start)'''

MAX = 27

'''start = perf_counter()
primes1 = sieve_Eratosthenes(MAX)
print(perf_counter()-start)'''

start = perf_counter()
primes2 = sieve_Pritchards_wheel(MAX)
print(perf_counter()-start)

print(primes2)
