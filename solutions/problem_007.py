'''By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we
can see that the 6th prime is 13.

What is the 10001st prime number?
'''
from math import log, ceil, sqrt, floor
from resources.useful_functions import sieve_Eratosthenes
global upper_bound


def primes_up_to(n, prime_list):
    '''Returns the list of primes up to the square root of n.'''
    end = floor(sqrt(n))
    ls = []
    for i in prime_list:
        if i > end:
            break
        ls.append(i)
    return ls


def nth_prime(n):
    '''Returns the nth prime number. Creates a list progressively of
    primes in order to do the checking in an easier manner. The list
    could be stored in a file to further use, but I didn't feel like it
    was necessary. I may implement it in the future.
    '''
    prime_list = [2, 3, 5, 7, 11, 13]
    if n <= 6:
        return prime_list[n - 1]
    # Not needed to divide by 2 or 3, we take numbers of the form
    # 6*j + 1 and 6*j - 1
    prime_list = prime_list[2:]
    # upper bound derived from Rosser's theorem (found in Wikipedia)
    # only valid for n >= 6
    for j in range(18, upper_bound + 2, 6):
        for k in (j - 1, j + 1):
            for p in primes_up_to(k, prime_list):
                if k % p == 0:
                    break
            else:
                prime_list.append(k)
        if len(prime_list) >= n - 2:
            break
    return prime_list[n - 3]


def nth_prime_v2(n):
    '''Returns the nth prime number using the Sieve of Eratosthenes.'''
    primes = sieve_Eratosthenes(upper_bound)
    return primes[n-1]


if __name__ == '__main__':
    N = 10001
    # https://arxiv.org/PS_cache/arxiv/pdf/1002/1002.0442v1.pdf
    upper_bound = ceil(N*(log(N) + log(log(N)) - 1/2))
    print(nth_prime(6))  # 13
    # print(nth_prime(N))  # 104743, 0.69s
    print(nth_prime_v2(N))  # 104743, 0.007s
