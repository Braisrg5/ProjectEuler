'''https://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we
can see that the 6th prime is 13.

What is the 10001st prime number?
'''
from math import log, ceil, sqrt, floor
from resources.useful_functions import sieve_Eratosthenes


def primes_up_to(n, prime_list):
    '''Returns the list of primes up to the square root of n.'''
    end = floor(sqrt(n))
    ls = []
    for i in prime_list:
        if i > end:
            break
        ls.append(i)
    return ls


def nth_prime_v2(N):
    '''Returns the nth prime number using the Sieve of Eratosthenes.'''
    # https://arxiv.org/PS_cache/arxiv/pdf/1002/1002.0442v1.pdf
    upper_bound = ceil((N+1)*(log(N+1) + log(log(N+1)) - 1/2))
    primes = sieve_Eratosthenes(upper_bound)
    return primes[N-1]


if __name__ == '__main__':
    print(nth_prime_v2(6))  # 13
    print(nth_prime_v2(10001))  # 104743, 0.007s
