'''It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.
                9=7+2*12
                15=7+2*22
                21=3+2*32
                25=7+2*32
                27=19+2*22
                33=31+2*12
It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
'''
from math import floor, sqrt, ceil


def sieveEratosthenes_mod(N):
    '''Returns a list of primes up to N. It also returns a list of composite
    odds for this particular problem.
    '''
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    for i in range(2, floor(sqrt(N))+1):
        if sieve[i]:
            for j in range(i*i, N+1, i):
                sieve[j] = False
        if i == 2:
            odds = [i for i in range(3, N+1) if sieve[i]]
    primes = [i for i in range(2, N+1) if sieve[i]]
    composite = list(set(odds)-set(primes))
    return primes, composite


def prime_twice_square(N, primes):
    '''Returns a list of numbers that can be written as the sum of a prime and
    twice a square.
    '''
    '''combinations = []
    for i in primes:
        maxj = ceil(sqrt(N-i)/2)
        for j in range(1,maxj+1):
            combinations.append(i+2*j**2)'''
    return [i+2*j**2 for i in primes for j in range(1, ceil(sqrt((N-i)/2)))]


def missing_odd_composite(N):
    primes, composite = sieveEratosthenes_mod(N)
    # We exclude the first prime (2) because of the problem statement
    # because 2 plus twice a square is not odd.
    ptwicesq = prime_twice_square(N, primes[1:])
    return list(set(composite)-set(ptwicesq))[0]


if __name__ == "__main__":
    print(missing_odd_composite(6000))  # 5777, 0.004s
