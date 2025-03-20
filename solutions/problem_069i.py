'''https://projecteuler.net/problem=69'''
# Euler's totient function, phi(n) [sometimes called the phi function], is
# defined as the number of positive integers not exceeding n which are
# relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less
# than or equal to nine and relatively prime to nine, phi(9) = 6.

#       n   Relatively prime    phi(n)  n/phi(n)
#       2         1               1        2
#       3        1,2              2       1.5
#       4        1,3              2        2
#       5      1,2,3,4            4       1.25
#       6        1,5              2        3
#       7    1,2,3,4,5,6          6      1.16666
#       8      1,3,5,7            4        2
#       9    1,2,4,5,7,8          6       1.5
#      10      1,3,7,9            4       2.5

# It can be seen that n=6 produces a maximum value of n/phi(n) for n<=10

# Find the value of n<= 1000000 for which n/phi(n) is a maximum.
from collections import Counter
from resources.useful_functions import sieve_Eratosthenes


def totient_values(bound):
    '''Finds all the values of the totient function for n <= bound.'''
    def prime_factors(n, list_fact=0):
        """Constructs an ordered list of the prime factors of a number n
        The factors are generated recursively, starting with an empty list.
        Once a factor is found, it is appended to the list, the number is
        divided by it and the function rerun."""
        if list_fact == 0:
            list_fact = []
        # If n is equal to 1, there are no more prime factors
        if n == 1:
            return list_fact

        # If n is a prime number, add it to the list and return
        if n in primes:
            return list_fact + [n]

        # Modified version: list of primes preloaded
        for p in primes:
            if n % p == 0:
                return prime_factors(n // p, list_fact + [p])
        return None

    primes = sieve_Eratosthenes(bound + 1)

    # The "function" is going to be a dictionary
    tot_func = {}
    for n in range(2, bound + 1):
        factors = Counter(prime_factors(n))
        phi_n = 1
        for p, exp in factors.items():
            phi_n *= p**(exp - 1)*(p - 1)
        tot_func[n] = n/phi_n
    return max(tot_func, key=tot_func.get)


def totient_values_v2(bound, bound_primes=100):
    '''Finds the n <= bound for which the ratio n/phi(n) is the largest as
    explained in (2*).'''
    # Arbitrary first nth primes (big enough for any real case)
    primes = sieve_Eratosthenes(bound_primes)
    num = 1
    for p in primes:
        num *= p
        if num > bound:
            return num//p
    # Not enough primes
    return -1


def main():
    '''Main code of module.'''
    print(totient_values(10))  # 6
    # print(totient_values(1000000))  # 510510, 30mins xd
    print(totient_values_v2(1000000))  # 510510, 0.000s


if __name__ == '__main__':
    main()


# ----- #
# Notes #
# ----- #

# (1*)
# https://en.wikipedia.org/wiki/Euler%27s_totient_function#Computing_Euler's_totient_function  # noqa
# If n = p1^k1 * p2^k2 * ... * pr^kr, then:
#           phi(n) = p1^(k1-1)*(p1-1)*...*pr^(kr-1)*(pr-1)

# (2*)
# If n = p1^k1*...*pr^kr, and phi(n) = p1^(k1-1)*(p1-1)*...*pr^(kr-1)*(pr-1),
# then:
#          n/phi(n) = p1^k1/(p1^(k1-1)*(p1-1)) * ... * pr^kr/(pr^(kr-1)*(pr-1))
# or:
#          n/phi(n) = p1/(p1-1)*p2/(p2-1)*...*pr/(pr-1)
# We need to maximize each of the factors, so let's compare two of them:
#          pi/(pi-1) > pj/(pj-1) <-> pi*pj - pi > pi*pj - pj <-> pi < pj
# So, we need to choose the set of primes as small as possible. It is trivial
# to see that these primes are going to be the first nth primes such that
#          p1*p2*...*pn <= bound
