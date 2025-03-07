'''https://projecteuler.net/problem=27'''
# Euler discovered the remarkable quadratic formula:
#                 n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive
# integer values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 =
# 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41
# is clearly divisible by 41.

# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
# primes for the consecutive values 0 <= n <= 79. The product of the
# coefficients, -79 and 1601, is -126479.

# Considering quadratics of the form:
#             n^2 + an + b, where |a| < 1000 and |b| <= 1000
#             where |n| is the modulus/absolute value of n
#             e.g. |11| = 11 and |-4| = 4.
# Find the product of the coefficients, a and b, for the quadratic
# expression that produces the maximum number of primes for consecutive
# values of n, starting with n = 0.
from resources.useful_functions import sieve_Eratosthenes, is_prime


def consecutive_primes(a, b):
    '''Finds the number of consecutive primes that produces the formula
    n^2 + an + b, starting with n = 0.'''
    n = 0
    val = b
    # We expect to eventually find a value that is not prime
    while is_prime(val):
        n += 1
        val = n*n + a*n + b
        if val <= 0:
            return n
    return n


def max_cons_primes_v2(bound):
    '''Finds the pair (a, b) that produces the maximum number of primes
    in the formula n^2 + an + b, starting with n = 0, where
    |a| < bound and |b| <= bound.
    Does so by observing that b and a + b + 1 have to be primes (1*).
    '''
    def consecutive_primes_v2(a, b):
        '''Finds the number of consecutive primes that produces the formula
        n^2 + an + b, starting with n = 0.'''
        # We already know b and a + b + 1 to be primes, so we start with n = 2
        n, val = 2, 2*2 + a*2 + b

        # If the new value is prime
        while val in set_primes:
            # We can increase n
            n += 1
            # and calculate the next value
            val = n*n + a*n + b
        # If val is not prime, n is equal to the number of consecutive primes
        return n

    # List of primes up to 2*bound + 2
    list_primes = sieve_Eratosthenes(2*bound + 2)
    # Set of primes for better performance
    set_primes = set(list_primes)
    d_primes = {}
    for p in list_primes:
        # Reached bound for p
        if p > bound:
            break
        # All possible values for p_prime
        for p_prime in list_primes:
            # Reached bound for p_prime
            if p_prime > bound + p + 1:
                break
            # We calculate a and b
            b, a = p, p_prime - p - 1
            # and find the number of consecutive primes in n^2 + an + b
            d_primes[(a, b)] = consecutive_primes_v2(a, b)
    # a and b that produce the maximum number of primes
    pair = max(d_primes, key=d_primes.get)
    return pair[0] * pair[1]


if __name__ == '__main__':
    print(consecutive_primes(1, 41))  # 40
    print(consecutive_primes(-79, 1601))  # 80
    print(max_cons_primes_v2(1000))  # (-61, 971), 0.04s


# ----- #
# Notes #
# ----- #

# (1*)
# When n = 0 then n^2 + an + b = b, and this has to be a prime, let's call it
# p. Also, when n = 1, n^2 + an + b = 1 + a + p, which is also a prime, let's
# call it p'. So, instead of looking for a and b, we can search for p and p':
#             |b| <= bound => -bound <= b <= bound => 0 < p <= bound (positive)
#             1 + a + p = p'  =>  a = p' - p - 1
#             |a| = |p' - p - 1| <= bound
#             -bound <= p' - p - 1 <= bound
#             -bound + p + 1 <= p' <= bound + p + 1
# p' has to be positive (it's a prime number), so, in summary, we need to
# find p and p' such that:
#             2 <= p <= bound
#             2 <= p' <= bound + p + 1
# And then calculate a and b.
# Observe that:
#             p' <= bound + p + 1 <= bound + bound + 1
# so, at most, p' <= 2*bound + 1. This will be the bound for the sieve.
